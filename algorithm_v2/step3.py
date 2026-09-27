"""
Algorithm V2 Step 3: Graph-Based Path Ordering

Creates a subgraph of selected courses, establishes prerequisite relationships,
and uses Yen's K-shortest paths algorithm to find optimal learning sequences.
"""
import logging
import time

from models.connection import get_graph
from utilities import query_algorithm_v2
from algorithm_v2 import step2

logger = logging.getLogger(__name__)


def _get_list_id(list_dictionary):
    return [d.get('id') for d in list_dictionary]


def add_new_label(courses):
    get_graph().run(query_algorithm_v2.add_new_label_for_courses_selected(courses))


def remove_label():
    get_graph().run(query_algorithm_v2.remove_label_selected())


def create_relationship_btw_courses(courses):
    get_graph().run(query_algorithm_v2.create_relationship_btw_courses_selected(courses))


def remove_relationship_btw_courses():
    get_graph().run(query_algorithm_v2.remove_relationship_btw_courses())


def create_sub_graph(user_id):
    get_graph().run(query_algorithm_v2.create_sub_graph_from_list_courses(user_id))


def remove_sub_graph(user_id):
    get_graph().run(query_algorithm_v2.remove_sub_graph(user_id))


def find_single_nodes():
    return get_graph().run(query_algorithm_v2.find_single_nodes_inside_sub_graph()).data()


def find_source_nodes():
    return get_graph().run(query_algorithm_v2.find_source_nodes_inside_sub_graph()).data()


def find_target_nodes():
    return get_graph().run(query_algorithm_v2.find_target_node_inside_sub_graph()).data()


def find_path_source_target(sources, targets, user_id):
    return get_graph().run(
        query_algorithm_v2.find_paths_from_sources_to_targets(sources, targets, user_id, 10)).data()


def check_existed_path_in_paths(paths, path_checked):
    for path in paths:
        if (path.get('sourceNodeName') == path_checked.get('sourceNodeName')
                and path.get('targetNodeName') == path_checked.get('targetNodeName')
                and path.get('totalCost') == path_checked.get('totalCost')):
            return True
    return False


def find_distinct_path(paths):
    """Find distinct paths, keeping only the longest cost path for each source-target pair."""
    paths_distinct = []
    for path in paths:
        path_selected = path
        for path_compare in paths:
            if (path.get('sourceNodeName') == path_compare.get('sourceNodeName')
                    and path.get('targetNodeName') == path_compare.get('targetNodeName')
                    and path.get('totalCost') < path_compare.get('totalCost')):
                path_selected = path_compare.copy()
        if not check_existed_path_in_paths(paths_distinct, path_selected):
            paths_distinct.append(path_selected)

    return [p.get('nodeNames') for p in paths_distinct]


def add_list_to_list(native_list, added_list):
    """Add elements from added_list to native_list, skipping duplicates."""
    for element in added_list:
        if element not in native_list:
            native_list.append(element)


def add_list_to_front_list(native_list, added_list):
    """Prepend added_list elements to native_list, maintaining order."""
    copy_native_list = native_list.copy()
    native_list.clear()
    native_list.extend(added_list)
    for element in copy_native_list:
        if element in native_list:
            native_list.remove(element)
            native_list.append(element)
        else:
            native_list.append(element)


def is_common_node_in_two_paths(path1, path2):
    for i in path1:
        if i in path2:
            return True
    return False


def get_common_node(path1, path2):
    for i in path1:
        if i in path2:
            if i == path1[0] or i == path2[0]:
                continue
            else:
                return i
    return 0


def are_lists_equal(list1, list2):
    """Check if two lists have identical contents (FIXED: name matches behavior)."""
    if len(list1) != len(list2):
        return False
    for i in range(len(list2)):
        if list1[i] != list2[i]:
            return False
    return True


def find_except_node(path_final):
    except_node = []
    for path in path_final:
        except_node.extend(path)
    return except_node


def get_target_common_source_path_two_element(paths, source, targets):
    """Process paths with common source that have exactly 2 elements."""
    targets_return = []
    sources_return = []

    for path in list(paths):  # FIXED: iterate over copy
        if source in path and len(path) == 2:
            add_list_to_list(targets_return, [path[1]])

    paths_to_remove = []
    for target in targets_return:
        if [source, target] in paths:
            paths_to_remove.append([source, target])

        for path in list(paths):  # FIXED: iterate over copy
            if path in paths_to_remove:
                continue
            if len(path) == 2 and path[1] == target:
                paths_to_remove.append(path)
                add_list_to_list(sources_return, [path[0]])
            elif len(path) >= 1 and path[-1] == target and path[0] == source:
                if len(path) >= 2:
                    targets.append(path[-2])
                paths_to_remove.append(path)
                if len(path) > 2:
                    paths.append(path[1:-1])
            elif len(path) > 1 and path[-1] == target:
                if len(path) >= 2:
                    targets.append(path[-2])
                paths_to_remove.append(path)
                paths.append(path[:-1])

        if target in targets:
            targets.remove(target)

    # Remove processed paths
    for path_removed in paths_to_remove:
        if path_removed in paths:
            paths.remove(path_removed)

    paths_to_remove_2 = []
    for path in list(paths):  # FIXED: iterate over copy
        if len(path) > 0 and path[0] == source:
            target_removed = path[-1]
            if target_removed in targets:
                targets.remove(target_removed)
            for inner_path in list(paths):  # FIXED: iterate over copy
                if (inner_path[0] != source and target_removed in inner_path
                        and len(inner_path) > 2
                        and inner_path[0] not in targets_return):
                    paths.append(inner_path[:-1])
                    targets.append(inner_path[-2])
                    paths_to_remove_2.append(inner_path)
            add_list_to_list(targets_return, path[1:])
            paths_to_remove_2.append(path)

    for path_removed in paths_to_remove_2:
        if path_removed in paths:
            paths.remove(path_removed)

    return sources_return + targets_return


def handle_path(paths, path_check, hash_map, path_final, new_hash_map):
    """Handle merging of paths with common nodes."""
    paths_have_common_node = [path_check]
    common_node = 0

    for path in list(paths):  # FIXED: iterate over copy
        if not are_lists_equal(path_check, path) and is_common_node_in_two_paths(path_check, path):
            if common_node == 0:
                common_node = get_common_node(path_check, path)
                paths_have_common_node.append(path.copy())
            elif get_common_node(path_check, path) == common_node:
                paths_have_common_node.append(path.copy())

    if len(paths_have_common_node) == 1:
        path_added = list(hash_map.get(path_check[0], []))
        path_added.extend(path_check)
        path_final.append(path_added)
        if path_check in paths:
            paths.remove(path_check)
        return

    sources = list(set(p[0] for p in paths_have_common_node))
    path_added = []
    for source in sources:
        path_added.extend(hash_map.get(source, []))

    for path in paths_have_common_node:
        if common_node != 0 and common_node in path:
            add_list_to_list(path_added, path[:path.index(common_node)])

    new_hash_map[common_node] = path_added


def is_in_path_final(node, path_final):
    """Check if a node appears anywhere in the final paths."""
    for outer in path_final:
        if node in outer:
            return True
    return False


def create_path_final(path_final, sources, targets, hash_map, user_id):
    """Recursively build final learning paths from source to target nodes."""
    if not sources:
        return

    # FIXED: remove items safely by building new lists instead of modifying during iteration
    targets = [t for t in targets if not is_in_path_final(t, path_final)]
    sources = [s for s in sources if not is_in_path_final(s, path_final)]

    if not sources or not targets:
        return

    raw_paths = find_path_source_target(sources, targets, user_id)
    paths = find_distinct_path(raw_paths)

    if not paths:
        return

    new_hash_map = {}

    # Handle 2-element paths first
    processed_sources = set()
    for path in list(paths):
        if len(path) == 2:
            source = path[0]
            if source not in processed_sources:
                processed_sources.add(source)
                targets_returned = get_target_common_source_path_two_element(paths, source, targets)
                base = hash_map.get(source, [])
                path_added = list(base) + [source] + targets_returned
                path_final.append(path_added)

    # Handle remaining paths
    for path in list(paths):
        if path in paths:  # May have been removed
            handle_path(paths, path, hash_map, path_final, new_hash_map)

    if new_hash_map:
        create_path_final(path_final, list(new_hash_map.keys()), targets, new_hash_map, user_id)


def _cleanup_graph(user_id):
    """Clean up temporary graph structures."""
    try:
        remove_sub_graph(user_id)
    except Exception:
        pass  # Sub-graph may not exist
    remove_label()
    remove_relationship_btw_courses()


def get_final_result(user_id):
    """Main entry point: generate ordered learning paths for a user."""
    start_step3 = time.time()

    set_courses = step2.get_input_for_step3(user_id)
    if not set_courses:
        logger.warning(f"No course sets found for user {user_id}")
        return []

    logger.info(f"Processing {len(set_courses)} course sets for user {user_id}")
    paths = []

    for set_course in set_courses:
        set_course = list(set(set_course))

        # Clean any previous state
        _cleanup_graph(user_id)

        try:
            add_new_label(set_course)
            create_relationship_btw_courses(set_course)
            create_sub_graph(user_id)

            path_final = []

            # Add single (isolated) nodes as standalone paths
            single_nodes = _get_list_id(find_single_nodes())
            for node in single_nodes:
                path_final.append([node])

            # Find source and target nodes for path building
            source_nodes = _get_list_id(find_source_nodes())
            target_nodes = _get_list_id(find_target_nodes())

            if source_nodes and target_nodes:
                hash_map = {node: [] for node in source_nodes}
                create_path_final(path_final, source_nodes, target_nodes, hash_map, user_id)
            elif source_nodes or target_nodes:
                # If only sources or targets exist, add them as linear paths
                for node in (source_nodes or target_nodes):
                    if not is_in_path_final(node, path_final):
                        path_final.append([node])

            paths.append(path_final)
        except Exception as e:
            logger.error(f"Error processing course set: {e}")
            paths.append([[c] for c in set_course])  # Fallback: unordered
        finally:
            _cleanup_graph(user_id)

    logger.info(f"Step 3 completed in {time.time() - start_step3:.2f}s, generated {len(paths)} paths")
    return paths
