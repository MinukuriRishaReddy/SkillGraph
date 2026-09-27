// ============================================================
// SKILL GRAPH DAG SEED DATA
// Learning Path Recommendation System
// ============================================================
// This script creates:
//   - 10 Career nodes
//   - Skill nodes (Knowledge, Tool, Platform, Framework, ProgramingLanguage)
//   - PREREQUISITE relationships between skills (DAG)
//   - NEED_* relationships from Careers to Skills
// ============================================================
// Compatible with existing model labels:
//   Career, Knowledge, Tool, Platform, Framework, ProgramingLanguage
// ============================================================

// ── 1. CREATE SKILL NODES ──────────────────────────────────
// Using MERGE to avoid duplicates if skills already exist.

// -- Programming Languages --
MERGE (:ProgramingLanguage {value: "HTML"});
MERGE (:ProgramingLanguage {value: "CSS"});
MERGE (:ProgramingLanguage {value: "JavaScript"});
MERGE (:ProgramingLanguage {value: "Python"});
MERGE (:ProgramingLanguage {value: "Java"});
MERGE (:ProgramingLanguage {value: "Kotlin"});
MERGE (:ProgramingLanguage {value: "Swift"});

// -- Frameworks --
MERGE (:Framework {value: "React"});
MERGE (:Framework {value: "Node.js"});
MERGE (:Framework {value: "Flutter"});
MERGE (:Framework {value: "React Native"});
MERGE (:Framework {value: "TensorFlow"});
MERGE (:Framework {value: "PyTorch"});

// -- Knowledge --
MERGE (:Knowledge {value: "Databases"});
MERGE (:Knowledge {value: "REST APIs"});
MERGE (:Knowledge {value: "System Design"});
MERGE (:Knowledge {value: "Statistics"});
MERGE (:Knowledge {value: "Data Analysis"});
MERGE (:Knowledge {value: "Machine Learning"});
MERGE (:Knowledge {value: "Deep Learning"});
MERGE (:Knowledge {value: "Data Visualization"});
MERGE (:Knowledge {value: "Linear Algebra"});
MERGE (:Knowledge {value: "Probability"});
MERGE (:Knowledge {value: "MLOps"});
MERGE (:Knowledge {value: "APIs"});
MERGE (:Knowledge {value: "Authentication"});
MERGE (:Knowledge {value: "Microservices"});
MERGE (:Knowledge {value: "UI/UX"});
MERGE (:Knowledge {value: "State Management"});
MERGE (:Knowledge {value: "Web Performance"});
MERGE (:Knowledge {value: "Networking"});
MERGE (:Knowledge {value: "Operating Systems"});
MERGE (:Knowledge {value: "Cryptography"});
MERGE (:Knowledge {value: "Ethical Hacking"});
MERGE (:Knowledge {value: "Threat Analysis"});
MERGE (:Knowledge {value: "Infrastructure as Code"});
MERGE (:Knowledge {value: "Cloud Security"});
MERGE (:Knowledge {value: "Mobile UI"});
MERGE (:Knowledge {value: "App Deployment"});
MERGE (:Knowledge {value: "Mathematics"});
MERGE (:Knowledge {value: "NLP"});
MERGE (:Knowledge {value: "Computer Vision"});
MERGE (:Knowledge {value: "AI Deployment"});

// -- Tools --
MERGE (:Tool {value: "Docker"});
MERGE (:Tool {value: "Kubernetes"});
MERGE (:Tool {value: "CI/CD"});
MERGE (:Tool {value: "Monitoring"});
MERGE (:Tool {value: "Security Tools"});
MERGE (:Tool {value: "Pandas"});
MERGE (:Tool {value: "NumPy"});
MERGE (:Tool {value: "Linux"});
MERGE (:Tool {value: "Containers"});

// -- Platforms --
MERGE (:Platform {value: "AWS"});
MERGE (:Platform {value: "Azure"});
MERGE (:Platform {value: "GCP"});
MERGE (:Platform {value: "Cloud Platforms"});


// ── 2. CREATE CAREER NODES ─────────────────────────────────

MERGE (:Career {creTitle: "Full Stack Developer"});
MERGE (:Career {creTitle: "Data Scientist"});
MERGE (:Career {creTitle: "Machine Learning Engineer"});
MERGE (:Career {creTitle: "Backend Developer"});
MERGE (:Career {creTitle: "Frontend Developer"});
MERGE (:Career {creTitle: "DevOps Engineer"});
MERGE (:Career {creTitle: "Cybersecurity Analyst"});
MERGE (:Career {creTitle: "Cloud Engineer"});
MERGE (:Career {creTitle: "Mobile App Developer"});
MERGE (:Career {creTitle: "AI Engineer"});


// ── 3. PREREQUISITE RELATIONSHIPS (DAG) ────────────────────
// Direction: (A)-[:PREREQUISITE]->(B) means "A is a prerequisite for B"
// i.e. you must learn A before B.

// -- Full Stack Developer path --
MATCH (a:ProgramingLanguage {value:"HTML"}), (b:ProgramingLanguage {value:"CSS"})
MERGE (a)-[:PREREQUISITE]->(b);

MATCH (a:ProgramingLanguage {value:"CSS"}), (b:ProgramingLanguage {value:"JavaScript"})
MERGE (a)-[:PREREQUISITE]->(b);

MATCH (a:ProgramingLanguage {value:"JavaScript"}), (b:Framework {value:"React"})
MERGE (a)-[:PREREQUISITE]->(b);

MATCH (a:ProgramingLanguage {value:"JavaScript"}), (b:Framework {value:"Node.js"})
MERGE (a)-[:PREREQUISITE]->(b);

MATCH (a:Framework {value:"Node.js"}), (b:Knowledge {value:"REST APIs"})
MERGE (a)-[:PREREQUISITE]->(b);

MATCH (a:Knowledge {value:"REST APIs"}), (b:Knowledge {value:"Databases"})
MERGE (a)-[:PREREQUISITE]->(b);

MATCH (a:Knowledge {value:"Databases"}), (b:Knowledge {value:"System Design"})
MERGE (a)-[:PREREQUISITE]->(b);

// -- Data Scientist path --
MATCH (a:ProgramingLanguage {value:"Python"}), (b:Knowledge {value:"Data Analysis"})
MERGE (a)-[:PREREQUISITE]->(b);

MATCH (a:Knowledge {value:"Statistics"}), (b:Knowledge {value:"Machine Learning"})
MERGE (a)-[:PREREQUISITE]->(b);

MATCH (a:Knowledge {value:"Data Analysis"}), (b:Tool {value:"Pandas"})
MERGE (a)-[:PREREQUISITE]->(b);

MATCH (a:Tool {value:"Pandas"}), (b:Tool {value:"NumPy"})
MERGE (a)-[:PREREQUISITE]->(b);

MATCH (a:Tool {value:"NumPy"}), (b:Knowledge {value:"Machine Learning"})
MERGE (a)-[:PREREQUISITE]->(b);

MATCH (a:Knowledge {value:"Machine Learning"}), (b:Knowledge {value:"Deep Learning"})
MERGE (a)-[:PREREQUISITE]->(b);

MATCH (a:Knowledge {value:"Data Analysis"}), (b:Knowledge {value:"Data Visualization"})
MERGE (a)-[:PREREQUISITE]->(b);

// -- Machine Learning Engineer path --
MATCH (a:ProgramingLanguage {value:"Python"}), (b:Knowledge {value:"Machine Learning"})
MERGE (a)-[:PREREQUISITE]->(b);

MATCH (a:Knowledge {value:"Linear Algebra"}), (b:Knowledge {value:"Machine Learning"})
MERGE (a)-[:PREREQUISITE]->(b);

MATCH (a:Knowledge {value:"Probability"}), (b:Knowledge {value:"Machine Learning"})
MERGE (a)-[:PREREQUISITE]->(b);

MATCH (a:Knowledge {value:"Deep Learning"}), (b:Framework {value:"TensorFlow"})
MERGE (a)-[:PREREQUISITE]->(b);

MATCH (a:Knowledge {value:"Deep Learning"}), (b:Framework {value:"PyTorch"})
MERGE (a)-[:PREREQUISITE]->(b);

MATCH (a:Framework {value:"TensorFlow"}), (b:Knowledge {value:"MLOps"})
MERGE (a)-[:PREREQUISITE]->(b);

MATCH (a:Framework {value:"PyTorch"}), (b:Knowledge {value:"MLOps"})
MERGE (a)-[:PREREQUISITE]->(b);

// -- Backend Developer path --
MATCH (a:ProgramingLanguage {value:"Python"}), (b:Knowledge {value:"APIs"})
MERGE (a)-[:PREREQUISITE]->(b);

MATCH (a:ProgramingLanguage {value:"Java"}), (b:Knowledge {value:"APIs"})
MERGE (a)-[:PREREQUISITE]->(b);

MATCH (a:Framework {value:"Node.js"}), (b:Knowledge {value:"APIs"})
MERGE (a)-[:PREREQUISITE]->(b);

MATCH (a:Knowledge {value:"APIs"}), (b:Knowledge {value:"Authentication"})
MERGE (a)-[:PREREQUISITE]->(b);

MATCH (a:Knowledge {value:"APIs"}), (b:Knowledge {value:"Databases"})
MERGE (a)-[:PREREQUISITE]->(b);

MATCH (a:Knowledge {value:"System Design"}), (b:Knowledge {value:"Microservices"})
MERGE (a)-[:PREREQUISITE]->(b);

// -- Frontend Developer path --
MATCH (a:Framework {value:"React"}), (b:Knowledge {value:"State Management"})
MERGE (a)-[:PREREQUISITE]->(b);

MATCH (a:Knowledge {value:"UI/UX"}), (b:Knowledge {value:"Web Performance"})
MERGE (a)-[:PREREQUISITE]->(b);

// -- DevOps Engineer path --
MATCH (a:Tool {value:"Linux"}), (b:Tool {value:"Docker"})
MERGE (a)-[:PREREQUISITE]->(b);

MATCH (a:Tool {value:"Docker"}), (b:Tool {value:"Kubernetes"})
MERGE (a)-[:PREREQUISITE]->(b);

MATCH (a:Knowledge {value:"Networking"}), (b:Platform {value:"Cloud Platforms"})
MERGE (a)-[:PREREQUISITE]->(b);

MATCH (a:Platform {value:"Cloud Platforms"}), (b:Tool {value:"CI/CD"})
MERGE (a)-[:PREREQUISITE]->(b);

MATCH (a:Tool {value:"CI/CD"}), (b:Tool {value:"Monitoring"})
MERGE (a)-[:PREREQUISITE]->(b);

// -- Cybersecurity Analyst path --
MATCH (a:Knowledge {value:"Networking"}), (b:Knowledge {value:"Operating Systems"})
MERGE (a)-[:PREREQUISITE]->(b);

MATCH (a:Knowledge {value:"Operating Systems"}), (b:Tool {value:"Security Tools"})
MERGE (a)-[:PREREQUISITE]->(b);

MATCH (a:Knowledge {value:"Cryptography"}), (b:Knowledge {value:"Ethical Hacking"})
MERGE (a)-[:PREREQUISITE]->(b);

MATCH (a:Knowledge {value:"Ethical Hacking"}), (b:Knowledge {value:"Threat Analysis"})
MERGE (a)-[:PREREQUISITE]->(b);

// -- Cloud Engineer path --
MATCH (a:Tool {value:"Linux"}), (b:Tool {value:"Containers"})
MERGE (a)-[:PREREQUISITE]->(b);

MATCH (a:Tool {value:"Containers"}), (b:Knowledge {value:"Infrastructure as Code"})
MERGE (a)-[:PREREQUISITE]->(b);

MATCH (a:Knowledge {value:"Infrastructure as Code"}), (b:Knowledge {value:"Cloud Security"})
MERGE (a)-[:PREREQUISITE]->(b);

// -- Mobile App Developer path --
MATCH (a:ProgramingLanguage {value:"Java"}), (b:ProgramingLanguage {value:"Kotlin"})
MERGE (a)-[:PREREQUISITE]->(b);

MATCH (a:ProgramingLanguage {value:"Swift"}), (b:Knowledge {value:"Mobile UI"})
MERGE (a)-[:PREREQUISITE]->(b);

MATCH (a:Knowledge {value:"Mobile UI"}), (b:Framework {value:"Flutter"})
MERGE (a)-[:PREREQUISITE]->(b);

MATCH (a:Knowledge {value:"Mobile UI"}), (b:Framework {value:"React Native"})
MERGE (a)-[:PREREQUISITE]->(b);

MATCH (a:Knowledge {value:"APIs"}), (b:Knowledge {value:"App Deployment"})
MERGE (a)-[:PREREQUISITE]->(b);

// -- AI Engineer path --
MATCH (a:Knowledge {value:"Mathematics"}), (b:Knowledge {value:"Machine Learning"})
MERGE (a)-[:PREREQUISITE]->(b);

MATCH (a:Knowledge {value:"Deep Learning"}), (b:Knowledge {value:"NLP"})
MERGE (a)-[:PREREQUISITE]->(b);

MATCH (a:Knowledge {value:"Deep Learning"}), (b:Knowledge {value:"Computer Vision"})
MERGE (a)-[:PREREQUISITE]->(b);

MATCH (a:Knowledge {value:"NLP"}), (b:Knowledge {value:"AI Deployment"})
MERGE (a)-[:PREREQUISITE]->(b);

MATCH (a:Knowledge {value:"Computer Vision"}), (b:Knowledge {value:"AI Deployment"})
MERGE (a)-[:PREREQUISITE]->(b);


// ── 4. CAREER → SKILL RELATIONSHIPS (NEED_*) ──────────────
// Using the existing relationship pattern: NEED_KNOWLEDGE, NEED_TOOL, etc.

// -- Full Stack Developer --
MATCH (c:Career {creTitle:"Full Stack Developer"}), (s:ProgramingLanguage {value:"HTML"}) MERGE (c)-[:NEED_PROGRAMINGLANGUAGE {Level:1}]->(s);
MATCH (c:Career {creTitle:"Full Stack Developer"}), (s:ProgramingLanguage {value:"CSS"}) MERGE (c)-[:NEED_PROGRAMINGLANGUAGE {Level:1}]->(s);
MATCH (c:Career {creTitle:"Full Stack Developer"}), (s:ProgramingLanguage {value:"JavaScript"}) MERGE (c)-[:NEED_PROGRAMINGLANGUAGE {Level:2}]->(s);
MATCH (c:Career {creTitle:"Full Stack Developer"}), (s:Framework {value:"React"}) MERGE (c)-[:NEED_FRAMEWORK {Level:2}]->(s);
MATCH (c:Career {creTitle:"Full Stack Developer"}), (s:Framework {value:"Node.js"}) MERGE (c)-[:NEED_FRAMEWORK {Level:2}]->(s);
MATCH (c:Career {creTitle:"Full Stack Developer"}), (s:Knowledge {value:"Databases"}) MERGE (c)-[:NEED_KNOWLEDGE {Level:2}]->(s);
MATCH (c:Career {creTitle:"Full Stack Developer"}), (s:Knowledge {value:"REST APIs"}) MERGE (c)-[:NEED_KNOWLEDGE {Level:2}]->(s);
MATCH (c:Career {creTitle:"Full Stack Developer"}), (s:Knowledge {value:"System Design"}) MERGE (c)-[:NEED_KNOWLEDGE {Level:3}]->(s);

// -- Data Scientist --
MATCH (c:Career {creTitle:"Data Scientist"}), (s:ProgramingLanguage {value:"Python"}) MERGE (c)-[:NEED_PROGRAMINGLANGUAGE {Level:2}]->(s);
MATCH (c:Career {creTitle:"Data Scientist"}), (s:Knowledge {value:"Statistics"}) MERGE (c)-[:NEED_KNOWLEDGE {Level:2}]->(s);
MATCH (c:Career {creTitle:"Data Scientist"}), (s:Knowledge {value:"Data Analysis"}) MERGE (c)-[:NEED_KNOWLEDGE {Level:2}]->(s);
MATCH (c:Career {creTitle:"Data Scientist"}), (s:Tool {value:"Pandas"}) MERGE (c)-[:NEED_TOOL {Level:2}]->(s);
MATCH (c:Career {creTitle:"Data Scientist"}), (s:Tool {value:"NumPy"}) MERGE (c)-[:NEED_TOOL {Level:2}]->(s);
MATCH (c:Career {creTitle:"Data Scientist"}), (s:Knowledge {value:"Machine Learning"}) MERGE (c)-[:NEED_KNOWLEDGE {Level:3}]->(s);
MATCH (c:Career {creTitle:"Data Scientist"}), (s:Knowledge {value:"Deep Learning"}) MERGE (c)-[:NEED_KNOWLEDGE {Level:3}]->(s);
MATCH (c:Career {creTitle:"Data Scientist"}), (s:Knowledge {value:"Data Visualization"}) MERGE (c)-[:NEED_KNOWLEDGE {Level:2}]->(s);

// -- Machine Learning Engineer --
MATCH (c:Career {creTitle:"Machine Learning Engineer"}), (s:ProgramingLanguage {value:"Python"}) MERGE (c)-[:NEED_PROGRAMINGLANGUAGE {Level:2}]->(s);
MATCH (c:Career {creTitle:"Machine Learning Engineer"}), (s:Knowledge {value:"Linear Algebra"}) MERGE (c)-[:NEED_KNOWLEDGE {Level:2}]->(s);
MATCH (c:Career {creTitle:"Machine Learning Engineer"}), (s:Knowledge {value:"Probability"}) MERGE (c)-[:NEED_KNOWLEDGE {Level:2}]->(s);
MATCH (c:Career {creTitle:"Machine Learning Engineer"}), (s:Knowledge {value:"Machine Learning"}) MERGE (c)-[:NEED_KNOWLEDGE {Level:3}]->(s);
MATCH (c:Career {creTitle:"Machine Learning Engineer"}), (s:Knowledge {value:"Deep Learning"}) MERGE (c)-[:NEED_KNOWLEDGE {Level:3}]->(s);
MATCH (c:Career {creTitle:"Machine Learning Engineer"}), (s:Framework {value:"TensorFlow"}) MERGE (c)-[:NEED_FRAMEWORK {Level:2}]->(s);
MATCH (c:Career {creTitle:"Machine Learning Engineer"}), (s:Framework {value:"PyTorch"}) MERGE (c)-[:NEED_FRAMEWORK {Level:2}]->(s);
MATCH (c:Career {creTitle:"Machine Learning Engineer"}), (s:Knowledge {value:"MLOps"}) MERGE (c)-[:NEED_KNOWLEDGE {Level:2}]->(s);

// -- Backend Developer --
MATCH (c:Career {creTitle:"Backend Developer"}), (s:ProgramingLanguage {value:"Python"}) MERGE (c)-[:NEED_PROGRAMINGLANGUAGE {Level:2}]->(s);
MATCH (c:Career {creTitle:"Backend Developer"}), (s:ProgramingLanguage {value:"Java"}) MERGE (c)-[:NEED_PROGRAMINGLANGUAGE {Level:2}]->(s);
MATCH (c:Career {creTitle:"Backend Developer"}), (s:Framework {value:"Node.js"}) MERGE (c)-[:NEED_FRAMEWORK {Level:2}]->(s);
MATCH (c:Career {creTitle:"Backend Developer"}), (s:Knowledge {value:"Databases"}) MERGE (c)-[:NEED_KNOWLEDGE {Level:2}]->(s);
MATCH (c:Career {creTitle:"Backend Developer"}), (s:Knowledge {value:"APIs"}) MERGE (c)-[:NEED_KNOWLEDGE {Level:2}]->(s);
MATCH (c:Career {creTitle:"Backend Developer"}), (s:Knowledge {value:"Authentication"}) MERGE (c)-[:NEED_KNOWLEDGE {Level:2}]->(s);
MATCH (c:Career {creTitle:"Backend Developer"}), (s:Knowledge {value:"System Design"}) MERGE (c)-[:NEED_KNOWLEDGE {Level:3}]->(s);
MATCH (c:Career {creTitle:"Backend Developer"}), (s:Knowledge {value:"Microservices"}) MERGE (c)-[:NEED_KNOWLEDGE {Level:3}]->(s);

// -- Frontend Developer --
MATCH (c:Career {creTitle:"Frontend Developer"}), (s:ProgramingLanguage {value:"HTML"}) MERGE (c)-[:NEED_PROGRAMINGLANGUAGE {Level:1}]->(s);
MATCH (c:Career {creTitle:"Frontend Developer"}), (s:ProgramingLanguage {value:"CSS"}) MERGE (c)-[:NEED_PROGRAMINGLANGUAGE {Level:1}]->(s);
MATCH (c:Career {creTitle:"Frontend Developer"}), (s:ProgramingLanguage {value:"JavaScript"}) MERGE (c)-[:NEED_PROGRAMINGLANGUAGE {Level:2}]->(s);
MATCH (c:Career {creTitle:"Frontend Developer"}), (s:Framework {value:"React"}) MERGE (c)-[:NEED_FRAMEWORK {Level:2}]->(s);
MATCH (c:Career {creTitle:"Frontend Developer"}), (s:Knowledge {value:"UI/UX"}) MERGE (c)-[:NEED_KNOWLEDGE {Level:2}]->(s);
MATCH (c:Career {creTitle:"Frontend Developer"}), (s:Knowledge {value:"State Management"}) MERGE (c)-[:NEED_KNOWLEDGE {Level:2}]->(s);
MATCH (c:Career {creTitle:"Frontend Developer"}), (s:Knowledge {value:"Web Performance"}) MERGE (c)-[:NEED_KNOWLEDGE {Level:2}]->(s);

// -- DevOps Engineer --
MATCH (c:Career {creTitle:"DevOps Engineer"}), (s:Tool {value:"Linux"}) MERGE (c)-[:NEED_TOOL {Level:2}]->(s);
MATCH (c:Career {creTitle:"DevOps Engineer"}), (s:Knowledge {value:"Networking"}) MERGE (c)-[:NEED_KNOWLEDGE {Level:2}]->(s);
MATCH (c:Career {creTitle:"DevOps Engineer"}), (s:Tool {value:"Docker"}) MERGE (c)-[:NEED_TOOL {Level:2}]->(s);
MATCH (c:Career {creTitle:"DevOps Engineer"}), (s:Tool {value:"Kubernetes"}) MERGE (c)-[:NEED_TOOL {Level:3}]->(s);
MATCH (c:Career {creTitle:"DevOps Engineer"}), (s:Tool {value:"CI/CD"}) MERGE (c)-[:NEED_TOOL {Level:2}]->(s);
MATCH (c:Career {creTitle:"DevOps Engineer"}), (s:Platform {value:"Cloud Platforms"}) MERGE (c)-[:NEED_PLATFORM {Level:2}]->(s);
MATCH (c:Career {creTitle:"DevOps Engineer"}), (s:Tool {value:"Monitoring"}) MERGE (c)-[:NEED_TOOL {Level:2}]->(s);

// -- Cybersecurity Analyst --
MATCH (c:Career {creTitle:"Cybersecurity Analyst"}), (s:Knowledge {value:"Networking"}) MERGE (c)-[:NEED_KNOWLEDGE {Level:2}]->(s);
MATCH (c:Career {creTitle:"Cybersecurity Analyst"}), (s:Knowledge {value:"Operating Systems"}) MERGE (c)-[:NEED_KNOWLEDGE {Level:2}]->(s);
MATCH (c:Career {creTitle:"Cybersecurity Analyst"}), (s:Knowledge {value:"Cryptography"}) MERGE (c)-[:NEED_KNOWLEDGE {Level:2}]->(s);
MATCH (c:Career {creTitle:"Cybersecurity Analyst"}), (s:Knowledge {value:"Ethical Hacking"}) MERGE (c)-[:NEED_KNOWLEDGE {Level:3}]->(s);
MATCH (c:Career {creTitle:"Cybersecurity Analyst"}), (s:Tool {value:"Security Tools"}) MERGE (c)-[:NEED_TOOL {Level:2}]->(s);
MATCH (c:Career {creTitle:"Cybersecurity Analyst"}), (s:Knowledge {value:"Threat Analysis"}) MERGE (c)-[:NEED_KNOWLEDGE {Level:3}]->(s);

// -- Cloud Engineer --
MATCH (c:Career {creTitle:"Cloud Engineer"}), (s:Tool {value:"Linux"}) MERGE (c)-[:NEED_TOOL {Level:2}]->(s);
MATCH (c:Career {creTitle:"Cloud Engineer"}), (s:Knowledge {value:"Networking"}) MERGE (c)-[:NEED_KNOWLEDGE {Level:2}]->(s);
MATCH (c:Career {creTitle:"Cloud Engineer"}), (s:Platform {value:"AWS"}) MERGE (c)-[:NEED_PLATFORM {Level:2}]->(s);
MATCH (c:Career {creTitle:"Cloud Engineer"}), (s:Platform {value:"Azure"}) MERGE (c)-[:NEED_PLATFORM {Level:2}]->(s);
MATCH (c:Career {creTitle:"Cloud Engineer"}), (s:Platform {value:"GCP"}) MERGE (c)-[:NEED_PLATFORM {Level:1}]->(s);
MATCH (c:Career {creTitle:"Cloud Engineer"}), (s:Tool {value:"Containers"}) MERGE (c)-[:NEED_TOOL {Level:2}]->(s);
MATCH (c:Career {creTitle:"Cloud Engineer"}), (s:Knowledge {value:"Infrastructure as Code"}) MERGE (c)-[:NEED_KNOWLEDGE {Level:2}]->(s);
MATCH (c:Career {creTitle:"Cloud Engineer"}), (s:Knowledge {value:"Cloud Security"}) MERGE (c)-[:NEED_KNOWLEDGE {Level:3}]->(s);

// -- Mobile App Developer --
MATCH (c:Career {creTitle:"Mobile App Developer"}), (s:ProgramingLanguage {value:"Java"}) MERGE (c)-[:NEED_PROGRAMINGLANGUAGE {Level:1}]->(s);
MATCH (c:Career {creTitle:"Mobile App Developer"}), (s:ProgramingLanguage {value:"Kotlin"}) MERGE (c)-[:NEED_PROGRAMINGLANGUAGE {Level:2}]->(s);
MATCH (c:Career {creTitle:"Mobile App Developer"}), (s:ProgramingLanguage {value:"Swift"}) MERGE (c)-[:NEED_PROGRAMINGLANGUAGE {Level:2}]->(s);
MATCH (c:Career {creTitle:"Mobile App Developer"}), (s:Framework {value:"Flutter"}) MERGE (c)-[:NEED_FRAMEWORK {Level:2}]->(s);
MATCH (c:Career {creTitle:"Mobile App Developer"}), (s:Framework {value:"React Native"}) MERGE (c)-[:NEED_FRAMEWORK {Level:2}]->(s);
MATCH (c:Career {creTitle:"Mobile App Developer"}), (s:Knowledge {value:"Mobile UI"}) MERGE (c)-[:NEED_KNOWLEDGE {Level:2}]->(s);
MATCH (c:Career {creTitle:"Mobile App Developer"}), (s:Knowledge {value:"APIs"}) MERGE (c)-[:NEED_KNOWLEDGE {Level:1}]->(s);
MATCH (c:Career {creTitle:"Mobile App Developer"}), (s:Knowledge {value:"App Deployment"}) MERGE (c)-[:NEED_KNOWLEDGE {Level:2}]->(s);

// -- AI Engineer --
MATCH (c:Career {creTitle:"AI Engineer"}), (s:ProgramingLanguage {value:"Python"}) MERGE (c)-[:NEED_PROGRAMINGLANGUAGE {Level:2}]->(s);
MATCH (c:Career {creTitle:"AI Engineer"}), (s:Knowledge {value:"Mathematics"}) MERGE (c)-[:NEED_KNOWLEDGE {Level:2}]->(s);
MATCH (c:Career {creTitle:"AI Engineer"}), (s:Knowledge {value:"Machine Learning"}) MERGE (c)-[:NEED_KNOWLEDGE {Level:3}]->(s);
MATCH (c:Career {creTitle:"AI Engineer"}), (s:Knowledge {value:"Deep Learning"}) MERGE (c)-[:NEED_KNOWLEDGE {Level:3}]->(s);
MATCH (c:Career {creTitle:"AI Engineer"}), (s:Knowledge {value:"NLP"}) MERGE (c)-[:NEED_KNOWLEDGE {Level:2}]->(s);
MATCH (c:Career {creTitle:"AI Engineer"}), (s:Knowledge {value:"Computer Vision"}) MERGE (c)-[:NEED_KNOWLEDGE {Level:2}]->(s);
MATCH (c:Career {creTitle:"AI Engineer"}), (s:Knowledge {value:"AI Deployment"}) MERGE (c)-[:NEED_KNOWLEDGE {Level:3}]->(s);


// ── 5. DAG VALIDATION QUERY ────────────────────────────────
// Run this after seeding to verify no cycles exist:
//
// MATCH path = (s)-[:PREREQUISITE*]->(s)
// RETURN count(path) AS cycles;
//
// Expected result: cycles = 0


// ── 6. EXAMPLE QUERIES ─────────────────────────────────────

// -- Fetch full learning path from a skill (all reachable prerequisites) --
// MATCH path = (start)-[:PREREQUISITE*]->(end)
// WHERE start.value = "HTML"
// RETURN [n IN nodes(path) | n.value] AS learning_path
// ORDER BY length(path) DESC
// LIMIT 5;

// -- Fetch all skills required for a career --
// MATCH (c:Career {creTitle: "Full Stack Developer"})-[r]->(s)
// WHERE type(r) STARTS WITH "NEED_"
// RETURN s.value AS skill, labels(s)[0] AS type, r.Level AS level
// ORDER BY r.Level;

// -- Topological ordering of skills for a career (learning order) --
// MATCH (c:Career {creTitle: "Data Scientist"})-[r]->(s)
// WHERE type(r) STARTS WITH "NEED_"
// WITH s
// OPTIONAL MATCH (prereq)-[:PREREQUISITE*]->(s)
// WITH s, count(prereq) AS depth
// RETURN s.value AS skill, labels(s)[0] AS type, depth
// ORDER BY depth ASC;

// -- Find what you need to learn given skills you already have --
// WITH ["Python", "Statistics"] AS known_skills
// MATCH (c:Career {creTitle: "Data Scientist"})-[r]->(s)
// WHERE type(r) STARTS WITH "NEED_" AND NOT s.value IN known_skills
// RETURN s.value AS skill_to_learn, labels(s)[0] AS type, r.Level AS level
// ORDER BY r.Level;
