"""
Expert Course Seeder for Neo4j AuraDB.
Uses MERGE and UNWIND for high performance and idempotency.
"""
import os, sys
import logging

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RecommendationSystem.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from dotenv import load_dotenv
load_dotenv()

from models.connection import get_graph

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

COURSES = [
    # Full Stack Developer
    {"name":"HTML & CSS Fundamentals","fee":0.0,"time":"20","rating":4.7,"enroll":52000,"link":"https://www.coursera.org/learn/html-css"},
    {"name":"JavaScript Essentials","fee":29.99,"time":"35","rating":4.6,"enroll":41000,"link":"https://www.udemy.com/course/javascript-essentials"},
    {"name":"React - The Complete Guide","fee":49.99,"time":"48","rating":4.8,"enroll":68000,"link":"https://www.udemy.com/course/react-complete-guide"},
    {"name":"Node.js Developer Course","fee":39.99,"time":"40","rating":4.5,"enroll":33000,"link":"https://www.udemy.com/course/nodejs-developer"},
    {"name":"RESTful API Design & Development","fee":29.99,"time":"22","rating":4.4,"enroll":18000,"link":"https://www.coursera.org/learn/restful-api"},
    {"name":"Database Systems Complete","fee":39.99,"time":"30","rating":4.5,"enroll":25000,"link":"https://www.coursera.org/learn/database-systems"},
    {"name":"System Design Fundamentals","fee":59.99,"time":"25","rating":4.6,"enroll":15000,"link":"https://www.educative.io/courses/system-design"},
    # Data Science
    {"name":"Python for Data Science","fee":0.0,"time":"30","rating":4.7,"enroll":95000,"link":"https://www.coursera.org/learn/python-data-science"},
    {"name":"Statistics and Probability","fee":49.99,"time":"28","rating":4.5,"enroll":30000,"link":"https://www.khanacademy.org/math/statistics"},
    {"name":"Data Analysis with Python","fee":39.99,"time":"32","rating":4.6,"enroll":42000,"link":"https://www.coursera.org/learn/data-analysis"},
    {"name":"Pandas & NumPy Masterclass","fee":29.99,"time":"20","rating":4.5,"enroll":28000,"link":"https://www.udemy.com/course/pandas-numpy"},
    {"name":"Data Visualization with Python","fee":29.99,"time":"18","rating":4.4,"enroll":22000,"link":"https://www.coursera.org/learn/data-viz"},
    # ML / AI
    {"name":"Linear Algebra for ML","fee":0.0,"time":"20","rating":4.6,"enroll":35000,"link":"https://www.khanacademy.org/math/linear-algebra"},
    {"name":"Probability and Statistics for ML","fee":0.0,"time":"22","rating":4.5,"enroll":28000,"link":"https://www.coursera.org/learn/probability-ml"},
    {"name":"Machine Learning by Stanford","fee":0.0,"time":"60","rating":4.9,"enroll":180000,"link":"https://www.coursera.org/learn/machine-learning"},
    {"name":"Deep Learning Specialization","fee":49.99,"time":"80","rating":4.8,"enroll":120000,"link":"https://www.coursera.org/specializations/deep-learning"},
    {"name":"TensorFlow Developer Certificate","fee":49.99,"time":"45","rating":4.7,"enroll":45000,"link":"https://www.coursera.org/professional-certificates/tensorflow"},
    {"name":"PyTorch for Deep Learning","fee":39.99,"time":"35","rating":4.6,"enroll":30000,"link":"https://www.udemy.com/course/pytorch-deep-learning"},
    {"name":"MLOps Engineering","fee":59.99,"time":"30","rating":4.4,"enroll":12000,"link":"https://www.coursera.org/learn/mlops"},
    {"name":"Mathematics for AI","fee":29.99,"time":"25","rating":4.5,"enroll":20000,"link":"https://www.coursera.org/learn/math-for-ai"},
    {"name":"NLP Specialization","fee":49.99,"time":"40","rating":4.7,"enroll":38000,"link":"https://www.coursera.org/specializations/nlp"},
    {"name":"Computer Vision with Deep Learning","fee":49.99,"time":"35","rating":4.6,"enroll":25000,"link":"https://www.coursera.org/learn/computer-vision"},
    {"name":"AI Deployment & Production","fee":39.99,"time":"28","rating":4.3,"enroll":10000,"link":"https://www.coursera.org/learn/ai-deployment"},
    # Backend
    {"name":"Python Backend Development","fee":39.99,"time":"40","rating":4.6,"enroll":35000,"link":"https://www.udemy.com/course/python-backend"},
    {"name":"Java Programming Masterclass","fee":49.99,"time":"50","rating":4.7,"enroll":55000,"link":"https://www.udemy.com/course/java-masterclass"},
    {"name":"API Design and Architecture","fee":29.99,"time":"20","rating":4.5,"enroll":16000,"link":"https://www.coursera.org/learn/api-design"},
    {"name":"Authentication & Security","fee":29.99,"time":"18","rating":4.4,"enroll":14000,"link":"https://www.udemy.com/course/auth-security"},
    {"name":"Microservices Architecture","fee":59.99,"time":"30","rating":4.5,"enroll":20000,"link":"https://www.udemy.com/course/microservices"},
    # Frontend
    {"name":"UI/UX Design Fundamentals","fee":29.99,"time":"22","rating":4.5,"enroll":30000,"link":"https://www.coursera.org/learn/ui-ux-design"},
    {"name":"Advanced React & State Management","fee":49.99,"time":"35","rating":4.7,"enroll":28000,"link":"https://www.udemy.com/course/advanced-react"},
    {"name":"Web Performance Optimization","fee":29.99,"time":"15","rating":4.3,"enroll":10000,"link":"https://www.udemy.com/course/web-performance"},
    # DevOps
    {"name":"Linux Administration","fee":29.99,"time":"30","rating":4.6,"enroll":40000,"link":"https://www.udemy.com/course/linux-admin"},
    {"name":"Docker & Containers","fee":29.99,"time":"22","rating":4.7,"enroll":45000,"link":"https://www.udemy.com/course/docker-containers"},
    {"name":"Kubernetes Mastery","fee":49.99,"time":"30","rating":4.6,"enroll":25000,"link":"https://www.udemy.com/course/kubernetes"},
    {"name":"Networking Fundamentals","fee":0.0,"time":"20","rating":4.4,"enroll":35000,"link":"https://www.coursera.org/learn/networking"},
    {"name":"Cloud Platforms Overview","fee":39.99,"time":"28","rating":4.5,"enroll":22000,"link":"https://www.coursera.org/learn/cloud-platforms"},
    {"name":"CI/CD Pipeline Mastery","fee":39.99,"time":"20","rating":4.5,"enroll":15000,"link":"https://www.udemy.com/course/cicd-pipelines"},
    {"name":"Infrastructure Monitoring","fee":29.99,"time":"18","rating":4.3,"enroll":10000,"link":"https://www.udemy.com/course/monitoring"},
    # Cybersecurity
    {"name":"Operating Systems Security","fee":29.99,"time":"25","rating":4.5,"enroll":18000,"link":"https://www.coursera.org/learn/os-security"},
    {"name":"Cryptography Fundamentals","fee":0.0,"time":"22","rating":4.6,"enroll":28000,"link":"https://www.coursera.org/learn/cryptography"},
    {"name":"Ethical Hacking Bootcamp","fee":49.99,"time":"45","rating":4.8,"enroll":55000,"link":"https://www.udemy.com/course/ethical-hacking"},
    {"name":"Security Tools & Penetration Testing","fee":39.99,"time":"30","rating":4.5,"enroll":20000,"link":"https://www.udemy.com/course/security-tools"},
    {"name":"Threat Analysis & Response","fee":49.99,"time":"25","rating":4.4,"enroll":12000,"link":"https://www.coursera.org/learn/threat-analysis"},
    # Cloud
    {"name":"AWS Certified Solutions Architect","fee":49.99,"time":"45","rating":4.7,"enroll":70000,"link":"https://www.udemy.com/course/aws-architect"},
    {"name":"Microsoft Azure Fundamentals","fee":0.0,"time":"20","rating":4.5,"enroll":40000,"link":"https://learn.microsoft.com/training/az-900"},
    {"name":"Google Cloud Fundamentals","fee":0.0,"time":"18","rating":4.4,"enroll":25000,"link":"https://www.coursera.org/learn/gcp-fundamentals"},
    {"name":"Infrastructure as Code with Terraform","fee":39.99,"time":"25","rating":4.6,"enroll":18000,"link":"https://www.udemy.com/course/terraform"},
    {"name":"Cloud Security Essentials","fee":39.99,"time":"22","rating":4.5,"enroll":14000,"link":"https://www.coursera.org/learn/cloud-security"},
    # Mobile
    {"name":"Kotlin for Android","fee":39.99,"time":"35","rating":4.6,"enroll":32000,"link":"https://www.udemy.com/course/kotlin-android"},
    {"name":"Swift & iOS Development","fee":49.99,"time":"40","rating":4.7,"enroll":38000,"link":"https://www.udemy.com/course/swift-ios"},
    {"name":"Flutter & Dart Complete Guide","fee":49.99,"time":"42","rating":4.8,"enroll":50000,"link":"https://www.udemy.com/course/flutter-dart"},
    {"name":"React Native - The Practical Guide","fee":49.99,"time":"38","rating":4.6,"enroll":35000,"link":"https://www.udemy.com/course/react-native"},
    {"name":"Mobile UI Design Patterns","fee":19.99,"time":"15","rating":4.4,"enroll":12000,"link":"https://www.udemy.com/course/mobile-ui"},
    {"name":"App Deployment & Publishing","fee":19.99,"time":"10","rating":4.3,"enroll":15000,"link":"https://www.udemy.com/course/app-deploy"},
]

# TEACH: course_name -> [(label, value, level), ...]
TEACH = {
    "HTML & CSS Fundamentals": [("ProgramingLanguage","HTML",1),("ProgramingLanguage","CSS",1)],
    "JavaScript Essentials": [("ProgramingLanguage","JavaScript",2)],
    "React - The Complete Guide": [("Framework","React",2),("Knowledge","State Management",1)],
    "Node.js Developer Course": [("Framework","Node.js",2)],
    "RESTful API Design & Development": [("Knowledge","REST APIs",2),("Knowledge","APIs",2)],
    "Database Systems Complete": [("Knowledge","Databases",2)],
    "System Design Fundamentals": [("Knowledge","System Design",3)],
    "Python for Data Science": [("ProgramingLanguage","Python",2),("Knowledge","Data Analysis",1)],
    "Statistics and Probability": [("Knowledge","Statistics",2),("Knowledge","Probability",2)],
    "Data Analysis with Python": [("Knowledge","Data Analysis",2)],
    "Pandas & NumPy Masterclass": [("Tool","Pandas",2),("Tool","NumPy",2)],
    "Data Visualization with Python": [("Knowledge","Data Visualization",2)],
    "Linear Algebra for ML": [("Knowledge","Linear Algebra",2)],
    "Probability and Statistics for ML": [("Knowledge","Probability",2),("Knowledge","Statistics",1)],
    "Machine Learning by Stanford": [("Knowledge","Machine Learning",3)],
    "Deep Learning Specialization": [("Knowledge","Deep Learning",3)],
    "TensorFlow Developer Certificate": [("Framework","TensorFlow",2)],
    "PyTorch for Deep Learning": [("Framework","PyTorch",2)],
    "MLOps Engineering": [("Knowledge","MLOps",2)],
    "Mathematics for AI": [("Knowledge","Mathematics",2),("Knowledge","Linear Algebra",1)],
    "NLP Specialization": [("Knowledge","NLP",2)],
    "Computer Vision with Deep Learning": [("Knowledge","Computer Vision",2)],
    "AI Deployment & Production": [("Knowledge","AI Deployment",3)],
    "Python Backend Development": [("ProgramingLanguage","Python",2),("Knowledge","APIs",1)],
    "Java Programming Masterclass": [("ProgramingLanguage","Java",2)],
    "API Design and Architecture": [("Knowledge","APIs",2),("Knowledge","REST APIs",1)],
    "Authentication & Security": [("Knowledge","Authentication",2)],
    "Microservices Architecture": [("Knowledge","Microservices",3),("Knowledge","System Design",2)],
    "UI/UX Design Fundamentals": [("Knowledge","UI/UX",2)],
    "Advanced React & State Management": [("Knowledge","State Management",2),("Framework","React",3)],
    "Web Performance Optimization": [("Knowledge","Web Performance",2)],
    "Linux Administration": [("Tool","Linux",2)],
    "Docker & Containers": [("Tool","Docker",2),("Tool","Containers",2)],
    "Kubernetes Mastery": [("Tool","Kubernetes",3)],
    "Networking Fundamentals": [("Knowledge","Networking",2)],
    "Cloud Platforms Overview": [("Platform","Cloud Platforms",2)],
    "CI/CD Pipeline Mastery": [("Tool","CI/CD",2)],
    "Infrastructure Monitoring": [("Tool","Monitoring",2)],
    "Operating Systems Security": [("Knowledge","Operating Systems",2)],
    "Cryptography Fundamentals": [("Knowledge","Cryptography",2)],
    "Ethical Hacking Bootcamp": [("Knowledge","Ethical Hacking",3)],
    "Security Tools & Penetration Testing": [("Tool","Security Tools",2)],
    "Threat Analysis & Response": [("Knowledge","Threat Analysis",3)],
    "AWS Certified Solutions Architect": [("Platform","AWS",2),("Platform","Cloud Platforms",1)],
    "Microsoft Azure Fundamentals": [("Platform","Azure",2)],
    "Google Cloud Fundamentals": [("Platform","GCP",2)],
    "Infrastructure as Code with Terraform": [("Knowledge","Infrastructure as Code",2)],
    "Cloud Security Essentials": [("Knowledge","Cloud Security",3)],
    "Kotlin for Android": [("ProgramingLanguage","Kotlin",2)],
    "Swift & iOS Development": [("ProgramingLanguage","Swift",2),("Knowledge","Mobile UI",1)],
    "Flutter & Dart Complete Guide": [("Framework","Flutter",2)],
    "React Native - The Practical Guide": [("Framework","React Native",2)],
    "Mobile UI Design Patterns": [("Knowledge","Mobile UI",2)],
    "App Deployment & Publishing": [("Knowledge","App Deployment",2)],
}

# REQUIRE: course_name -> [(label, value, level), ...]
REQUIRE = {
    "JavaScript Essentials": [("ProgramingLanguage","HTML",1),("ProgramingLanguage","CSS",1)],
    "React - The Complete Guide": [("ProgramingLanguage","JavaScript",1)],
    "Node.js Developer Course": [("ProgramingLanguage","JavaScript",1)],
    "RESTful API Design & Development": [("Framework","Node.js",1)],
    "Database Systems Complete": [("Knowledge","APIs",1)],
    "System Design Fundamentals": [("Knowledge","Databases",1)],
    "Data Analysis with Python": [("ProgramingLanguage","Python",1)],
    "Pandas & NumPy Masterclass": [("Knowledge","Data Analysis",1)],
    "Data Visualization with Python": [("Knowledge","Data Analysis",1)],
    "Machine Learning by Stanford": [("ProgramingLanguage","Python",1),("Knowledge","Statistics",1)],
    "Deep Learning Specialization": [("Knowledge","Machine Learning",2)],
    "TensorFlow Developer Certificate": [("Knowledge","Deep Learning",2)],
    "PyTorch for Deep Learning": [("Knowledge","Deep Learning",2)],
    "MLOps Engineering": [("Knowledge","Machine Learning",2)],
    "NLP Specialization": [("Knowledge","Deep Learning",2)],
    "Computer Vision with Deep Learning": [("Knowledge","Deep Learning",2)],
    "AI Deployment & Production": [("Knowledge","Machine Learning",2)],
    "API Design and Architecture": [("ProgramingLanguage","Python",1)],
    "Authentication & Security": [("Knowledge","APIs",1)],
    "Microservices Architecture": [("Knowledge","System Design",1)],
    "Advanced React & State Management": [("Framework","React",1)],
    "Web Performance Optimization": [("Knowledge","UI/UX",1)],
    "Docker & Containers": [("Tool","Linux",1)],
    "Kubernetes Mastery": [("Tool","Docker",1)],
    "Cloud Platforms Overview": [("Knowledge","Networking",1)],
    "CI/CD Pipeline Mastery": [("Platform","Cloud Platforms",1)],
    "Infrastructure Monitoring": [("Tool","CI/CD",1)],
    "Operating Systems Security": [("Knowledge","Networking",1)],
    "Ethical Hacking Bootcamp": [("Knowledge","Cryptography",1)],
    "Security Tools & Penetration Testing": [("Knowledge","Operating Systems",1)],
    "Threat Analysis & Response": [("Knowledge","Ethical Hacking",2)],
    "Infrastructure as Code with Terraform": [("Tool","Containers",1)],
    "Cloud Security Essentials": [("Knowledge","Infrastructure as Code",1)],
    "Kotlin for Android": [("ProgramingLanguage","Java",1)],
    "Flutter & Dart Complete Guide": [("Knowledge","Mobile UI",1)],
    "React Native - The Practical Guide": [("ProgramingLanguage","JavaScript",1),("Knowledge","Mobile UI",1)],
    "App Deployment & Publishing": [("Knowledge","APIs",1)],
}

REL_MAP = {
    "Knowledge": "KNOWLEDGE",
    "Tool": "TOOL",
    "Platform": "PLATFORM",
    "Framework": "FRAMEWORK",
    "ProgramingLanguage": "PROGRAMINGLANGUAGE",
}

def run_seeding():
    g = get_graph()

    # 1. Bulk Create/Update Courses using UNWIND (High Performance)
    logger.info(f"Seeding {len(COURSES)} courses using UNWIND...")
    course_query = """
    UNWIND $batch AS row
    MERGE (c:Course {crsLink: row.link})
    ON CREATE SET 
        c.crsName = row.name,
        c.crsFee = row.fee,
        c.crsTime = row.time,
        c.crsRating = row.rating,
        c.crsEnroll = row.enroll
    ON MATCH SET
        c.crsName = row.name,
        c.crsFee = row.fee,
        c.crsTime = row.time,
        c.crsRating = row.rating,
        c.crsEnroll = row.enroll
    """
    g.run(course_query, batch=COURSES)

    # 2. Create TEACH relationships
    logger.info("Seeding TEACH_* relationships...")
    for crs_name, skills in TEACH.items():
        for label, value, level in skills:
            rel_type = f"TEACH_{REL_MAP[label]}"
            # Using MERGE for idempotency
            query = f"""
            MATCH (c:Course {{crsName: $crs}})
            MATCH (s:{label} {{value: $val}})
            MERGE (c)-[r:{rel_type}]->(s)
            ON CREATE SET r.Level = $lvl
            ON MATCH SET r.Level = $lvl
            """
            g.run(query, crs=crs_name, val=value, lvl=level)

    # 3. Create REQUIRE relationships
    logger.info("Seeding REQUIRE_* relationships...")
    for crs_name, skills in REQUIRE.items():
        for label, value, level in skills:
            rel_type = f"REQUIRE_{REL_MAP[label]}"
            query = f"""
            MATCH (c:Course {{crsName: $crs}})
            MATCH (s:{label} {{value: $val}})
            MERGE (c)-[r:{rel_type}]->(s)
            ON CREATE SET r.Level = $lvl
            ON MATCH SET r.Level = $lvl
            """
            g.run(query, crs=crs_name, val=value, lvl=level)

    # 4. Verification
    logger.info("Verifying database state...")
    try:
        summary = g.run("""
            MATCH (n:Course)
            RETURN count(n) AS courses, 
                   size([(n)-[r]->() WHERE type(r) STARTS WITH 'TEACH_' | r]) AS teach_rels,
                   size([(n)-[r]->() WHERE type(r) STARTS WITH 'REQUIRE_' | r]) AS require_rels
        """).data()
        
        # Note: Summing results because of list comprehension above
        courses = g.run("MATCH (n:Course) RETURN count(n) AS c").data()[0]['c']
        t_count = g.run("MATCH (n:Course)-[r]->() WHERE type(r) STARTS WITH 'TEACH_' RETURN count(r) AS c").data()[0]['c']
        r_count = g.run("MATCH (n:Course)-[r]->() WHERE type(r) STARTS WITH 'REQUIRE_' RETURN count(r) AS c").data()[0]['c']
        
        print("\n" + "="*30)
        print("SEEDING COMPLETE")
        print("="*30)
        print(f"  Courses Created/Matched  : {courses}")
        print(f"  TEACH_* Relationships   : {t_count}")
        print(f"  REQUIRE_* Relationships : {r_count}")
        print("="*30 + "\n")
    except Exception as e:
        logger.error(f"Verification failed: {e}")

if __name__ == '__main__':
    run_seeding()
