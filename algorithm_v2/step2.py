"""
Algorithm V2 Step 2: Genetic Algorithm Optimization

Optimizes course sets using a genetic algorithm with:
- Population initialization from candidate courses
- Fitness evaluation (weighted multi-objective)
- Selection of top performers
- Crossover and mutation operators
- Cost/time constraint filtering
"""
import random
import math
import time
import logging

from py2neo.matching import NodeMatcher

from models.user import User
from models.connection import get_graph
from constants.algorithm_constants import AlgorithmConstant
from utilities.query_for_algorithm import (
    query_get_user_need_lo, query_to_get_list_lo_provided_by_set_course,
    query_get_list_time_of_set_course, query_get_sum_tuition_set_course
)
from utilities.query_for_services import query_get_user_info
from algorithm_v2 import step1

logger = logging.getLogger(__name__)


# ==================== CORE GENETIC ALGORITHM ====================

def run_genetic_algorithm(all_set_of_candidate_course, user):
    """Run the genetic algorithm to find optimized course sets."""
    LO_imax = finding_length_of_population(all_set_of_candidate_course)
    if not LO_imax:
        logger.warning("Cannot find LO_imax")
        return []

    length_of_native_population = LO_imax[1]
    native_population = initial_population(all_set_of_candidate_course, LO_imax)
    if not native_population:
        return []

    optimized_population = []
    for _ in range(AlgorithmConstant.V2_GENETIC_LOOP_TIMES):
        optimized_population = evaluate_and_filter(native_population, length_of_native_population, user)
        if not optimized_population:
            return []
        n = len(optimized_population)
        while n < length_of_native_population:
            optimized_population = rebuild_population(optimized_population, all_set_of_candidate_course, user)
            n = len(optimized_population)
            if n > length_of_native_population:
                optimized_population.pop()
                break

    return optimized_population


def finding_optimization_courses(all_set_of_candidate_course, user):
    """Find optimized course sets, filtered by user constraints."""
    user_need_time = user.time
    user_need_cost = user.cost

    optimized_population = run_genetic_algorithm(all_set_of_candidate_course, user)
    if not optimized_population:
        logger.warning("Cannot find course sets from genetic algorithm")
        return []

    # Extract course sets from individuals
    optimized_set_of_course = []
    for individual in optimized_population:
        courses = get_set_of_course_from_individual(individual)
        if courses is not None:
            optimized_set_of_course.append(courses)

    if not optimized_set_of_course:
        return []

    # Apply user constraints
    filter_set_of_course = optimized_set_of_course
    if user_need_time != 0:
        filter_set_of_course = user_filter_time(user_need_time, optimized_set_of_course)
    elif user_need_cost != 0:
        filter_set_of_course = user_filter_cost(user_need_cost, optimized_set_of_course)

    # Deduplicate and limit to OMEGA
    returned = []
    for element in filter_set_of_course:
        element_sorted = sorted(element)
        if element_sorted not in returned:
            returned.append(element_sorted)
        if len(returned) == AlgorithmConstant.V2_OMEGA:
            break
    return returned


# ==================== POPULATION MANAGEMENT ====================

def finding_length_of_population(all_set_of_candidate_course):
    """Find the LO with the maximum number of candidate courses."""
    max_length = 0
    LO_imax = []
    for i, set_of_candidate_course in enumerate(all_set_of_candidate_course):
        if len(set_of_candidate_course) > max_length:
            max_length = len(set_of_candidate_course)
            LO_imax = [i, max_length]
    if not LO_imax:
        logger.warning("Cannot find LO_imax in finding_length_of_population")
    return LO_imax or None


def initial_population(all_set_of_candidate_course, LO_imax):
    """Create the initial population from candidate courses."""
    imax_index = LO_imax[0]
    s = LO_imax[1]
    native_population = []

    for stop_point in range(s):
        individual = []
        for i, set_of_candidate_course in enumerate(all_set_of_candidate_course):
            if i != imax_index:
                length = len(set_of_candidate_course)
                if stop_point > length - 1:
                    j = random.randint(0, length - 1)
                else:
                    j = stop_point
                individual.append(set_of_candidate_course[j])
            else:
                individual.append(set_of_candidate_course[stop_point])
        native_population.append(individual)

    if not native_population:
        logger.warning("Cannot create initial population")
    return native_population


def evaluate_and_filter(native_population, length_of_population, user):
    """Evaluate fitness and select top performers."""
    scores = {}
    for i, individual in enumerate(native_population):
        scores[i] = calculate_score_for_individual(individual, user)

    sorted_indices = sorted(scores.keys(), key=lambda k: scores[k])
    n = math.floor(AlgorithmConstant.V2_LAMBDA * length_of_population)
    n = max(n, 1)  # At least 1

    selected_indices = sorted_indices[:n]
    return [native_population[i] for i in selected_indices]


def rebuild_population(optimized_population, all_set_of_candidate_course, user):
    """Add new individuals via crossover or mutation."""
    n = len(optimized_population)
    if n < 1:
        return optimized_population

    if n < 2:
        # Only one individual — generate new ones via mutation
        individual = list(optimized_population[0])
        length_of_individual_gen = len(all_set_of_candidate_course)
        i = random.randint(0, length_of_individual_gen - 1)
        new_individual = mutate(individual, all_set_of_candidate_course[i], i)
        optimized_population.append(new_individual)
        return optimized_population

    index_1 = random.randint(0, n - 1)
    index_2 = random.randint(0, n - 1)
    while index_1 == index_2:
        index_2 = random.randint(0, n - 1)

    # CRITICAL FIX: deep copy individuals before modifying
    individual_1 = list(optimized_population[index_1])
    individual_2 = list(optimized_population[index_2])

    ratio = random.random()
    if ratio > AlgorithmConstant.V2_ALPHA:
        new_individuals = crossover(individual_1, individual_2)
        optimized_population.append(new_individuals[0])
        optimized_population.append(new_individuals[1])
    else:
        length_of_individual_gen = len(all_set_of_candidate_course)
        i = random.randint(0, length_of_individual_gen - 1)
        new_individual_1 = mutate(individual_1, all_set_of_candidate_course[i], i)
        new_individual_2 = mutate(individual_2, all_set_of_candidate_course[i], i)
        optimized_population.append(new_individual_1)
        optimized_population.append(new_individual_2)
    return optimized_population


def mutate(individual, set_of_course, i):
    """Mutate an individual by replacing one gene. Returns a NEW individual."""
    new_individual = list(individual)  # FIXED: copy before mutating
    mutate_point_index = random.randint(0, len(set_of_course) - 1)
    new_individual[i] = set_of_course[mutate_point_index]
    return new_individual


def crossover(individual_1, individual_2):
    """Crossover two individuals at the midpoint. Returns NEW individuals."""
    # FIXED: work on copies, not originals
    child_1 = list(individual_1)
    child_2 = list(individual_2)
    crossover_point = math.floor((len(child_1) - 1) / 2)
    for i in range(crossover_point + 1):
        child_1[i], child_2[i] = child_2[i], child_1[i]
    return [child_1, child_2]


# ==================== FITNESS FUNCTIONS ====================

def calculate_score_for_set_of_course(set_of_course, user):
    """Calculate weighted fitness score for a course set."""
    user_lo_need = get_graph().run(query_get_user_need_lo(user.id)).data()
    f1 = calculate_number_of_course(set_of_course)
    f2 = calculate_number_of_redundant_LO(set_of_course, user_lo_need)
    f3 = calculate_number_of_overlap_LO(set_of_course)
    f4 = calculate_number_of_overlap_level(set_of_course, user_lo_need)
    return (f1 * AlgorithmConstant.V2_W1 +
            f2 * AlgorithmConstant.V2_W2 +
            f3 * AlgorithmConstant.V2_W3 +
            f4 * AlgorithmConstant.V2_W4)


def calculate_score_for_individual(individual, user):
    """Calculate fitness score for a genetic algorithm individual."""
    set_of_course = get_set_of_course_from_individual(individual)
    if set_of_course is None:
        return float('inf')
    return calculate_score_for_set_of_course(set_of_course, user)


def calculate_number_of_course(set_of_course):
    return len(set(set_of_course))


def calculate_number_of_redundant_LO(set_of_course, user_lo_need):
    lo_provided = get_graph().run(query_to_get_list_lo_provided_by_set_course(set_of_course)).data()
    set_lo = list(set(_get_list_id(lo_provided)))
    return len(set_lo) - len(user_lo_need)


def calculate_number_of_overlap_LO(set_of_course):
    lo_provided = get_graph().run(query_to_get_list_lo_provided_by_set_course(set_of_course)).data()
    set_lo = list(set(_get_list_id(lo_provided)))
    return len(lo_provided) - len(set_lo)


def calculate_number_of_overlap_level(set_of_course, user_lo_need):
    counter = 0
    lo_provided = get_graph().run(query_to_get_list_lo_provided_by_set_course(set_of_course)).data()
    for lo in user_lo_need:
        for lo_p in lo_provided:
            if lo.get('id') == lo_p.get('id'):
                counter += lo_p.get('level', 0) - lo.get('level', 0)
                break
    return counter


def calculate_sum_time_of_individual(set_of_course):
    list_time = get_graph().run(query_get_list_time_of_set_course(set_of_course)).data()
    total_time = 0
    for t in list_time:
        try:
            time_str = t.get('time', '')
            if time_str and ' ' in time_str:
                total_time += float(time_str[:time_str.find(" ")])
            elif time_str:
                total_time += float(time_str)
        except (ValueError, TypeError):
            pass
    return total_time


def calculate_sum_cost_of_individual(set_of_course):
    sumFee = get_graph().run(query_get_sum_tuition_set_course(set_of_course)).data()
    return sumFee[0].get('sumFee') or 0


# ==================== CONSTRAINT FILTERS ====================

def user_filter_time(user_need_time, optimized_set_of_course):
    return [s for s in optimized_set_of_course
            if user_need_time >= calculate_sum_time_of_individual(s)]


def user_filter_cost(user_need_cost, optimized_set_of_course):
    return [s for s in optimized_set_of_course
            if user_need_cost >= calculate_sum_cost_of_individual(s)]


# ==================== UTILITY FUNCTIONS ====================

def _get_list_id(list_dict):
    return [d.get('id') for d in list_dict]


def get_set_of_course_from_individual(individual):
    """Extract flat list of course IDs from a genetic algorithm individual."""
    course_list = []
    for gen in individual:
        if isinstance(gen, list):
            course_list.extend(gen)
        elif isinstance(gen, int):
            course_list.append(gen)
        else:
            # Try to handle Candidate objects
            try:
                course_list.extend(gen.get_value())
            except AttributeError:
                logger.warning(f"Unknown gene type in individual: {type(gen)}")
                return None
    return list(set(course_list))


# ==================== STEP 2 → STEP 3 INTERFACE ====================

def get_input_for_step3(user_id):
    """Generate optimized course sets for step 3."""
    start_step2 = time.time()

    # Get candidates from step 1
    sets_of_course = step1.get_input_for_step2(user_id)
    all_set_of_candidate_course = []
    for set_of_course in sets_of_course:
        by_lo = [candidate_course.get_value() for candidate_course in set_of_course]
        all_set_of_candidate_course.append(by_lo)

    if not all_set_of_candidate_course:
        logger.warning("No candidate courses found")
        return []

    # Build user object
    try:
        user_data = get_graph().run(query_get_user_info(user_id)).data()
        if not user_data:
            logger.error(f"User {user_id} not found")
            return []
        user = User(user_data[0])
        user.id = user_id
    except Exception as e:
        logger.error(f"Error loading user {user_id}: {e}")
        return []

    result = finding_optimization_courses(all_set_of_candidate_course, user)
    if not result:
        return []

    # Sort by score
    scored = []
    for courses in result:
        scored.append({
            'courses': courses,
            'score': calculate_score_for_set_of_course(courses, user)
        })
    scored.sort(key=lambda d: d['score'])

    logger.info(f"Step 2 completed in {time.time() - start_step2:.2f}s")
    return [s['courses'] for s in scored]
