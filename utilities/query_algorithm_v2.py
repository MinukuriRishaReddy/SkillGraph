"""Cypher query builders for Algorithm V2."""


def query_get_user_need_lo(user_id):
    return (f"MATCH (u:User)-[r]->(k) "
            f"WHERE ID(u) = {int(user_id)} AND TYPE(r) =~ 'NEED_.*' "
            f"RETURN id(k) AS id, r.Level AS level;")


def query_get_user_lo(user_id):
    return (f"MATCH (u:User)-[r]->(k) "
            f"WHERE ID(u) = {int(user_id)} AND (TYPE(r) =~ 'NEED_.*' OR TYPE(r) =~'HAS_.*') AND TYPE(r) <> 'HAS_OBJECTIVE' "
            f"RETURN id(k) AS id, r.Level AS level;")


def query_get_lo_provided_by_course(course_id):
    return (f'MATCH (lo) <- [r2] - (c:Course) '
            f'WHERE id(c) = {int(course_id)} '
            f'AND TYPE(r2) =~ "TEACH_.*" '
            f'RETURN id(lo) AS id, r2.Level AS level')


def query_get_input_lo_of_a_course(course_id):
    return (f'MATCH (c:Course)-[r]->(lo) '
            f'WHERE id(c) = {int(course_id)} AND TYPE(r) =~ "REQUIRE_.*" '
            f'RETURN id(lo) AS id, r.Level AS level')


def query_get_courses_provided_a_lo(lo_id, level):
    return (f'MATCH (lo)<-[r]-(c:Course) '
            f'MATCH (lo1)<-[r1]-(c1:Course)-[r2]->(lo1) '
            f'WHERE type(r1) =~ "REQUIRE.*" AND type(r2) =~ "TEACH.*" '
            f'WITH lo, c, r, collect(id(c1)) AS except '
            f'WHERE id(lo) = {int(lo_id)} AND r.Level >= {int(level)} AND NOT id(c) IN except '
            f'AND type(r) =~ "TEACH.*" RETURN id(c) AS id')


def query_get_top_courses_with_overlap_similarity(user_id, courses, muy):
    return (f'MATCH (p1:User)-[ru]-(e1) '
            f'WHERE type(ru) <> "HAS_OBJECTIVE" AND id(p1) = {int(user_id)} '
            f'WITH p1, collect(id(e1)) AS p1entity_type, {list(courses)} AS courses '
            f'MATCH (p2:Course)-[rc]-(e2) '
            f'WHERE (type(rc) =~ "TEACH_.*" OR type(rc) =~ "REQUIRE_.*") AND id(p2) IN courses '
            f'WITH p1, p1entity_type, p2, collect(id(e2)) AS p2entity_type '
            f'WITH p2, p1entity_type, p2entity_type, '
            f'toFloat(size([x IN p1entity_type WHERE x IN p2entity_type])) AS intersection, '
            f'toFloat(CASE WHEN size(p1entity_type) < size(p2entity_type) THEN size(p1entity_type) ELSE size(p2entity_type) END) AS minSize '
            f'WHERE minSize > 0 AND intersection > 0 '
            f'RETURN id(p2) AS id, intersection / minSize AS similarity '
            f'ORDER BY similarity DESC '
            f'LIMIT {int(muy)}')


# ================= Step 3 ========================

def add_new_label_for_courses_selected(courses):
    return (f'WITH {list(courses)} AS course '
            f'MATCH (c:Course) '
            f'WHERE id(c) IN course '
            f'SET c:Selected;')


def remove_label_selected():
    return ('MATCH (n:Selected) '
            'REMOVE n:Selected')


def create_relationship_btw_courses_selected(courses):
    return (f'WITH {list(courses)} AS courses '
            f'MATCH (c:Course)-[r]->(lo)<-[r1]-(c1:Course) '
            f'WHERE type(r) =~ "REQUIRE.*" AND type(r1) =~ "TEACH.*" AND id(c) IN courses '
            f'AND id(c1) IN courses AND id(c) <> id(c1) '
            f'MERGE (c1)-[:SELECTED {{weight: 1}}]->(c);')


def remove_relationship_btw_courses():
    return ('MATCH ()-[r:SELECTED]->() '
            'DELETE r;')


def create_sub_graph_from_list_courses(user_id):
    # No-op: GDS graph projection not needed; queries use :Selected label directly
    return 'RETURN 1'


def remove_sub_graph(user_id):
    # No-op: no in-memory GDS graph to drop
    return 'RETURN 1'


def find_single_nodes_inside_sub_graph():
    return ('MATCH (s:Selected)<-[r]-(s1:Selected) '
            'WHERE type(r) = "SELECTED" '
            'WITH collect(id(s)) AS target, collect(id(s1)) AS source '
            'MATCH (s2:Selected) '
            'WHERE NOT (id(s2) IN target) AND NOT (id(s2) IN source) '
            'RETURN id(s2) AS id')


def find_source_nodes_inside_sub_graph():
    return ('MATCH (s:Selected)<-[r]-(s1:Selected) '
            'WHERE type(r) = "SELECTED" '
            'WITH collect(id(s)) AS target, collect(id(s1)) AS source '
            'MATCH (s2:Selected) '
            'WHERE NOT (id(s2) IN target) AND id(s2) IN source '
            'RETURN id(s2) AS id')


def find_target_node_inside_sub_graph():
    return ('MATCH (s:Selected)<-[r]-(s1:Selected) '
            'WHERE type(r) = "SELECTED" '
            'WITH collect(id(s1)) AS source, collect(id(s)) AS target '
            'MATCH (s2:Selected) '
            'WHERE NOT (id(s2) IN source) AND id(s2) IN target '
            'RETURN id(s2) AS id')


def find_paths_from_sources_to_targets(sources, targets, user_id, k):
    max_depth = 20
    return (f'WITH {list(sources)} AS nodeSource, {list(targets)} AS nodeTarget '
            f'MATCH (source:Selected), (target:Selected) '
            f'WHERE id(source) IN nodeSource AND id(target) IN nodeTarget '
            f'MATCH path = (source)-[:SELECTED*1..{max_depth}]->(target) '
            f'WITH source, target, path, '
            f'reduce(cost = 0, r IN relationships(path) | cost + r.weight) AS totalCost, '
            f'[n IN nodes(path) | id(n)] AS nodeNames '
            f'RETURN id(source) AS sourceNodeName, '
            f'id(target) AS targetNodeName, '
            f'totalCost, nodeNames '
            f'ORDER BY id(source), id(target), totalCost DESC '
            f'LIMIT {int(k) * len(sources) * len(targets)}')
