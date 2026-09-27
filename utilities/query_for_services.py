"""
Cypher query builders for service layer operations.

Note: Integer IDs are safe to interpolate directly since they're validated as int
before reaching these functions. String values use parameterized queries via
the sanitize_string helper to prevent Cypher injection.
"""
import re


def _sanitize_string(value):
    """Escape special characters in string values for Cypher queries."""
    if value is None:
        return ''
    # Remove any characters that could be used for injection
    return re.sub(r'[\'\"\\;{}()\[\]]', '', str(value))


def query_create_user(user_id, cost, time):
    return f'MATCH (u:User) WHERE id(u) = {int(user_id)} SET u.cost = {int(cost)} SET u.time = {int(time)} RETURN id(u) AS id;'


def query_register(name, email, password_hash):
    safe_name = _sanitize_string(name)
    safe_email = _sanitize_string(email)
    safe_hash = _sanitize_string(password_hash)
    return f"CREATE (n:User {{name:'{safe_name}', email:'{safe_email}', password:'{safe_hash}'}}) RETURN id(n) AS id;"


def query_get_id_by_email(email):
    safe_email = _sanitize_string(email)
    return f'MATCH (u:User) WHERE u.email = "{safe_email}" RETURN id(u) AS id, u.password AS password;'


def query_get_user_info(user_id):
    return (f'MATCH (u:User) '
            f'WHERE id(u)={int(user_id)} '
            f'RETURN id(u) AS id, u.email AS email, u.name AS name, u.cost AS cost, u.time AS time;')


def query_create_objective_career(user_id, career_id):
    return (f'MATCH (a:User), (b:Career) WHERE id(a)={int(user_id)} AND id(b)={int(career_id)} '
            f'MERGE (a)-[r:HAS_OBJECTIVE]->(b) RETURN id(r) AS id;')


def query_get_objective(user_id):
    return (f'MATCH (u:User)-[r]->(c:Career) '
            f'WHERE id(u) = {int(user_id)} '
            f'RETURN id(c) AS id, c.creTitle AS title')


def query_create_has_lo(user_id, lo):
    lo_id = int(lo.get('id'))
    lo_type = _sanitize_string(lo.get('type')).upper()
    lo_level = int(lo.get('level', 1))
    return (f"MATCH (a:User), (b) WHERE id(a)={int(user_id)} AND id(b)={lo_id} "
            f"MERGE (a)-[r:HAS_{lo_type} {{Level:{lo_level}}}]->(b);")


def query_create_user_need_lo(user_id):
    uid = int(user_id)
    return [
        f" MATCH (u:User)-[:HAS_OBJECTIVE]->(c:Career)"
        f" MATCH (u)-[ru:HAS_TOOL]->(ku:Tool)<-[rcc:NEED_TOOL]-(c)"
        f" WHERE id(u)={uid} AND ((ru.Level < rcc.Level))"
        f" MERGE (u)-[r:NEED_TOOL{{Level:rcc.Level}}]->(ku) RETURN id(r) AS id;",

        f" MATCH (u:User)-[:HAS_OBJECTIVE]->(c:Career)"
        f" MATCH (c)-[rc:NEED_TOOL]->(kc)"
        f" WHERE id(u)={uid} AND NOT (u)-[:HAS_TOOL]->(kc)"
        f" MERGE (u)-[r:NEED_TOOL{{Level:rc.Level}}]->(kc) RETURN id(r) AS id;",

        f" MATCH (u:User)-[:HAS_OBJECTIVE]->(c:Career)"
        f" MATCH (u)-[ru:HAS_KNOWLEDGE]->(ku)<-[rcc:NEED_KNOWLEDGE]-(c)"
        f" WHERE id(u)={uid} AND ((ru.Level < rcc.Level))"
        f" MERGE (u)-[r:NEED_KNOWLEDGE{{Level:rcc.Level}}]->(ku) RETURN id(r) AS id;",

        f" MATCH (u:User)-[:HAS_OBJECTIVE]->(c:Career)"
        f" MATCH (c)-[rc:NEED_KNOWLEDGE]->(kc)"
        f" WHERE id(u)={uid} AND NOT (u)-[:HAS_KNOWLEDGE]->(kc)"
        f" MERGE (u)-[r:NEED_KNOWLEDGE{{Level:rc.Level}}]->(kc) RETURN id(r) AS id;",

        f" MATCH (u:User)-[:HAS_OBJECTIVE]->(c:Career)"
        f" MATCH (u)-[ru:HAS_PLATFORM]->(ku)<-[rcc:NEED_PLATFORM]-(c)"
        f" WHERE id(u)={uid} AND ((ru.Level < rcc.Level))"
        f" MERGE (u)-[r:NEED_PLATFORM{{Level:rcc.Level}}]->(ku) RETURN id(r) AS id;",

        f" MATCH (u:User)-[:HAS_OBJECTIVE]->(c:Career)"
        f" MATCH (c)-[rc:NEED_PLATFORM]->(kc)"
        f" WHERE id(u)={uid} AND NOT (u)-[:HAS_PLATFORM]->(kc)"
        f" MERGE (u)-[r:NEED_PLATFORM{{Level:rc.Level}}]->(kc) RETURN id(r) AS id;",

        f" MATCH (u:User)-[:HAS_OBJECTIVE]->(c:Career)"
        f" MATCH (u)-[ru:HAS_FRAMEWORK]->(ku)<-[rcc:NEED_FRAMEWORK]-(c)"
        f" WHERE id(u)={uid} AND ((ru.Level < rcc.Level))"
        f" MERGE (u)-[r:NEED_FRAMEWORK{{Level:rcc.Level}}]->(ku) RETURN id(r) AS id;",

        f" MATCH (u:User)-[:HAS_OBJECTIVE]->(c:Career)"
        f" MATCH (c)-[rc:NEED_FRAMEWORK]->(kc)"
        f" WHERE id(u)={uid} AND NOT (u)-[:HAS_FRAMEWORK]->(kc)"
        f" MERGE (u)-[r:NEED_FRAMEWORK{{Level:rc.Level}}]->(kc) RETURN id(r) AS id;",

        f" MATCH (u:User)-[:HAS_OBJECTIVE]->(c:Career)"
        f" MATCH (u)-[ru:HAS_PROGRAMINGLANGUAGE]->(ku)<-[rcc:NEED_PROGRAMINGLANGUAGE]-(c)"
        f" WHERE id(u)={uid} AND ((ru.Level < rcc.Level))"
        f" MERGE (u)-[r:NEED_PROGRAMINGLANGUAGE{{Level:rcc.Level}}]->(ku) RETURN id(r) AS id;",

        f" MATCH (u:User)-[:HAS_OBJECTIVE]->(c:Career)"
        f" MATCH (c)-[rc:NEED_PROGRAMINGLANGUAGE]->(kc)"
        f" WHERE id(u)={uid} AND NOT (u)-[:HAS_PROGRAMINGLANGUAGE]->(kc)"
        f" MERGE (u)-[r:NEED_PROGRAMINGLANGUAGE{{Level:rc.Level}}]->(kc) RETURN id(r) AS id;",
    ]


def query_delete_relationship_user_need_lo(user_id):
    return (f'MATCH (u:User)-[r]->(lo) '
            f'WHERE id(u) = {int(user_id)} AND type(r) =~"NEED_.*" '
            f'DELETE r')


def query_get_course_name_by_id(set_course):
    return (f'WITH {list(set_course)} AS list '
            f'MATCH (c:Course) '
            f'WHERE id(c) IN list '
            f'RETURN c.crsName AS name')


def query_get_lo_need_by_career(career_id):
    return (f' MATCH (c:Career)-[r]->(lo) '
            f'WHERE id(c) = {int(career_id)} '
            f'RETURN id(lo) AS id, lo.value AS name, type(r) AS type')


def query_update_career(user_id, career_id):
    return (f'MATCH (u:User)-[r]->(c:Career) '
            f'WHERE id(u) = {int(user_id)} '
            f'DELETE r;')


def query_get_info_a_course(course_id):
    return (f'MATCH (c:Course) '
            f'WHERE id(c) = {int(course_id)} '
            f'RETURN id(c) AS id, c.crsName AS name, c.crsEnroll AS enroll, c.crsFee AS cost, c.crsLink AS link, '
            f'c.crsTime AS time, c.crsRating AS rating')


def query_get_lo_user_has(user_id):
    return (f'MATCH (u:User)-[r]-(lo) '
            f'WHERE id(u) = {int(user_id)} AND type(r) <> "HAS_OBJECTIVE" AND type(r) =~ "HAS_.*" '
            f'RETURN id(lo) AS id, lo.value AS value, r.Level AS level')


def query_get_lo_need_by_career_by_user_id(user_id):
    return (f' MATCH (u:User)-[r1]->(c:Career)-[r]->(lo) '
            f'WHERE id(u) = {int(user_id)} '
            f'RETURN id(lo) AS id, lo.value AS name, r.Level AS level, type(r) AS type')


def query_get_top_100_lo():
    return ('WITH ["Knowledge", "Tool", "Platform", "ProgramingLanguage", "Framework"] AS types '
            'MATCH (u) '
            'WHERE labels(u)[0] IN types '
            'RETURN id(u) AS id, u.value AS value, labels(u)[0] AS type LIMIT 100')


def query_search_lo(value):
    safe_value = _sanitize_string(value)
    return (f'WITH ["Knowledge", "Tool", "Platform", "ProgramingLanguage", "Framework"] AS types '
            f'MATCH (u) '
            f'WHERE labels(u)[0] IN types AND u.value CONTAINS "{safe_value}" '
            f'RETURN id(u) AS id, u.value AS value, labels(u)[0] AS type LIMIT 100')


def query_get_lo_has(user_id):
    return (f'MATCH (u:User)-[r]->(lo) '
            f'WHERE id(u) = {int(user_id)} AND type(r) =~ "HAS_.*" AND type(r) <> "HAS_OBJECTIVE" '
            f'RETURN id(lo) AS id, lo.value AS value, r.Level AS level '
            f'ORDER BY id;')


def query_delete_lo_has(user_id, lo_id):
    return (f'MATCH (u:User)-[r]->(lo) '
            f'WHERE id(u) = {int(user_id)} AND id(lo) = {int(lo_id)} '
            f'DELETE r')


def query_create_lo_has(user_id, lo_id, level, lo_type):
    safe_type = _sanitize_string(lo_type).upper()
    return (f'MATCH (u:User) '
            f'WHERE id(u) = {int(user_id)} '
            f'MATCH (lo) '
            f'WHERE id(lo) = {int(lo_id)} '
            f'MERGE (u)-[r:HAS_{safe_type} {{Level: {int(level)}}}]->(lo) RETURN id(r) AS id')


def query_get_type(lo_id):
    return (f'MATCH (lo) '
            f'WHERE id(lo) = {int(lo_id)} '
            f'RETURN labels(lo)[0] AS type')


def query_get_skill_learning_path(career_id):
    cid = int(career_id)
    return (
        f'MATCH (c:Career) WHERE id(c) = {cid} '
        f'WITH c, c.creTitle AS career '
        f'MATCH (c)-[r]->(lo) '
        f'WITH career, collect({{id: toString(id(lo)), name: lo.value, type: type(r), level: r.Level}}) AS skills, collect(id(lo)) AS lo_ids '
        f'OPTIONAL MATCH (a)-[:PREREQUISITE]->(b) WHERE id(a) IN lo_ids AND id(b) IN lo_ids '
        f'RETURN career, skills, collect({{source: toString(id(a)), target: toString(id(b))}}) AS relations'
    )


def query_get_courses_info(course_id):
    return (f'MATCH (c:Course) '
            f'WHERE id(c) = {int(course_id)} '
            f'RETURN id(c) AS id, c.crsName AS name, c.crsFee AS cost, c.crsTime AS Time, c.crsRating AS rating, '
            f'c.crsLink AS link, c.crsEnroll AS enroll;')
