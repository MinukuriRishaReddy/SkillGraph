"""
Seed the Neo4j database with Skill Graph DAG data.

Usage:
    python seed_graph.py

Requires Neo4j to be running and .env configured.
"""
import os
import sys
import re

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RecommendationSystem.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from dotenv import load_dotenv
load_dotenv()

from models.connection import get_graph


def load_cypher_file(filepath):
    """Parse a .cypher file into executable statements safely."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Remove comments
    content = re.sub(r'//.*', '', content)
    
    # 2. Split by semicolon that is NOT followed by text on the SAME line
    # This regex matches a semicolon followed by optional spaces and then a newline
    statements = []
    raw_statements = re.split(r';\s*(?=\n|$)', content)
    
    for stmt in raw_statements:
        cleaned = stmt.strip()
        if cleaned:
            # Re-add semicolon for the driver
            statements.append(cleaned + ';')
    return statements


def run_seed():
    graph = get_graph()
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Load both seed files
    files = ['seed_skill_graph.cypher', 'seed_courses.cypher']
    statements = []
    for f in files:
        path = os.path.join(base_dir, f)
        if os.path.exists(path):
            stmts = load_cypher_file(path)
            print(f"  Loaded {len(stmts)} statements from {f}")
            statements.extend(stmts)

    print(f"\nRunning {len(statements)} total Cypher statements...")

    success = 0
    errors = 0
    for i, stmt in enumerate(statements, 1):
        try:
            # We use transactional session for each statement
            graph.run(stmt)
            success += 1
        except Exception as e:
            errors += 1
            # Show context for the error
            print(f"  [{i}] ERROR: {e}")
            print(f"       Statement Start: {stmt[:100]}...")
            if len(stmt) > 100:
                print(f"       Statement End:   ...{stmt[-50:]}")

    print(f"\nDone: {success} succeeded, {errors} failed")

    # Validate DAG (no cycles)
    print("\nValidating DAG (checking for cycles)...")
    try:
        result = graph.run(
            "MATCH path = (s)-[:PREREQUISITE*]->(s) RETURN count(path) AS cycles"
        ).data()
        cycles = result[0]['cycles'] if result else 0
        if cycles == 0:
            print("  DAG is valid - no cycles detected!")
        else:
            print(f"  WARNING: {cycles} cycle(s) detected!")
    except:
        pass

    # Print summary
    print("\nGraph summary:")
    for label in ['Career', 'Knowledge', 'Tool', 'Platform', 'Framework', 'ProgramingLanguage', 'Course']:
        try:
            count = graph.run(f"MATCH (n:{label}) RETURN count(n) AS c").data()[0]['c']
            print(f"  {label}: {count} nodes")
        except:
            print(f"  {label}: 0 nodes")

    try:
        rel_types = graph.run("MATCH ()-[r]->() RETURN DISTINCT type(r) AS t").data()
        for r in rel_types:
            t = r['t']
            count = graph.run(f"MATCH ()-[r:{t}]->() RETURN count(r) AS c").data()[0]['c']
            print(f"  {t} relationships: {count}")
    except:
        pass


if __name__ == '__main__':
    run_seed()
