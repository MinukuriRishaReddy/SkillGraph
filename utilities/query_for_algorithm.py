"""Cypher query builders for Algorithm V1."""


# ========================= STEP 1 =================================

def query_get_user_need_lo(user_id):
    return (f"MATCH (u:User)-[r]->(k) "
            f"WHERE ID(u) = {int(user_id)} AND TYPE(r) =~ 'NEED_.*' "
            f"RETURN id(k) AS id, r.Level AS level;")


def query_get_user_need_lo_id(user_id):
    return (f"MATCH (u:User)-[r]->(k) "
            f"WHERE ID(u) = {int(user_id)} AND TYPE(r) =~ 'NEED_.*' "
            f"RETURN collect(id(k)) AS lo_list")


def query_get_user_lo(user_id):
    return (f"MATCH (u:User)-[r]->(k) "
            f"WHERE ID(u) = {int(user_id)} AND (TYPE(r) =~ 'NEED_.*' OR TYPE(r) =~ 'HAS_.*') AND TYPE(r) <> 'HAS_OBJECTIVE' "
            f"RETURN id(k) AS id, r.Level AS level;")


def query_get_lo_provided_by_course(course_id):
    return (f'MATCH (lo) <- [r2] - (c:Course) '
            f'WHERE id(c) = {int(course_id)} '
            f'AND TYPE(r2) =~ "TEACH_.*" '
            f'RETURN id(lo) AS id, lo.value AS name, r2.Level AS level')


def query_get_input_lo_of_a_course(course_id):
    return (f'MATCH (c:Course)-[r]->(lo) '
            f'WHERE id(c) = {int(course_id)} AND TYPE(r) =~ "REQUIRE_.*" '
            f'RETURN id(lo) AS id, r.Level AS level')


def query_get_rating_course(course_id):
    return f'MATCH (c:Course) WHERE id(c) = {int(course_id)} RETURN c.crsRating AS rating'


def query_get_courses_provided_a_lo(lo_id, level):
    return (f'MATCH (lo)<-[r]-(c:Course) WHERE id(lo) = {int(lo_id)} AND r.Level >= {int(level)} '
            f'AND type(r) =~ "TEACH.*" RETURN id(c) AS id')


def query_calculate_similarity_jaccard(user_id, course_id):
    return (f'MATCH (p1:User)-[ru]-(e1) '
            f'WHERE type(ru) =~ "NEED_.*" AND id(p1) = {int(user_id)} '
            f'WITH p1, collect(id(e1)) AS p1entity_type '
            f'MATCH (p2:Course)-[rc]-(e2) WHERE type(rc) =~ "TEACH_.*" AND id(p2) = {int(course_id)} '
            f'AND type(rc) <> "TEACH_IN" '
            f'WITH p1, p1entity_type, p2, collect(id(e2)) AS p2entity_type '
            f'WITH p1entity_type, p2entity_type, '
            f'toFloat(size([x IN p1entity_type WHERE x IN p2entity_type])) AS intersection '
            f'WITH intersection, toFloat(size(p1entity_type) + size(p2entity_type)) - intersection AS unionSize '
            f'RETURN CASE WHEN unionSize = 0 THEN 0.0 ELSE intersection / unionSize END AS similarity')


def query_calculate_similarity_overlap(user_id, course_id):
    return (f'MATCH (p1:User)-[ru]-(e1) '
            f'WHERE type(ru) =~ "NEED_.*" AND id(p1) = {int(user_id)} '
            f'WITH p1, collect(id(e1)) AS p1entity_type '
            f'MATCH (p2:Course)-[rc]-(e2) '
            f'WHERE (type(rc) =~ "TEACH_.*" OR type(rc) =~ "REQUIRE_.*") AND id(p2) = {int(course_id)} '
            f'AND type(rc) <> "TEACH_IN" '
            f'WITH p1, p1entity_type, p2, collect(id(e2)) AS p2entity_type '
            f'WITH p1entity_type, p2entity_type, '
            f'toFloat(size([x IN p1entity_type WHERE x IN p2entity_type])) AS intersection, '
            f'toFloat(CASE WHEN size(p1entity_type) < size(p2entity_type) THEN size(p1entity_type) ELSE size(p2entity_type) END) AS minSize '
            f'RETURN CASE WHEN minSize = 0 THEN 0.0 ELSE intersection / minSize END AS similarity')


# =============================== STEP 2 ==========================================

def query_lo_require_a_course(course_id):
    return (f'MATCH (c:Course)-[r]->(lo) '
            f'WHERE id(c) = {int(course_id)} AND TYPE(r) =~ "REQUIRE_.*" '
            f'RETURN id(lo) AS id, lo.value AS name, r.Level AS level')


def query_to_get_list_lo_provided_by_set_course(set_course_id):
    return (f'WITH {list(set_course_id)} AS listCourse '
            f'MATCH (lo)<-[r1]-(c:Course) '
            f'WHERE type(r1) =~ "TEACH_.*" AND id(c) IN listCourse '
            f'RETURN id(lo) AS id, r1.Level AS level')


def query_to_create_temporary_relationship_user_lo(user_id, list_lo):
    return (f'WITH {list(list_lo)} AS list '
            f'MATCH (a:User), (b) WHERE id(a) = {int(user_id)} AND id(b) IN list '
            f'CREATE (a)-[r:NEED_TEMPORARY {{Level:1}}]->(b);')


def query_to_remove_temporary_relationship_created(user_id):
    return (f'MATCH (a:User)-[r]->(b) WHERE id(a) = {int(user_id)} AND type(r) = "NEED_TEMPORARY" '
            f'DELETE r')


def query_get_rating_set_course(set_course_id):
    return (f'WITH {list(set_course_id)} AS listCourse '
            f'MATCH (c:Course) '
            f'WHERE id(c) IN listCourse '
            f'RETURN avg(c.crsRating) AS avgRating')


def query_get_sum_tuition_set_course(set_course_id):
    return (f'WITH {list(set_course_id)} AS listCourse '
            f'MATCH (c:Course) '
            f'WHERE id(c) IN listCourse '
            f'RETURN sum(c.crsFee) AS sumFee')


def query_get_list_time_of_set_course(set_course_id):
    return (f'WITH {list(set_course_id)} AS listCourse '
            f'MATCH (c:Course) '
            f'WHERE id(c) IN listCourse '
            f'RETURN c.crsTime AS time')


# ================================ STEP 4 ==========================================

def query_get_lo_user_has(user_id):
    return (f'MATCH (u:User)-[ru]->(m) '
            f'WHERE id(u) = {int(user_id)} AND type(ru) =~ "HAS_.*" AND type(ru) <> "HAS_OBJECTIVE" '
            f'RETURN id(m) AS id_lo, ru.Level AS level')
