// ============================================================
// COURSE SEED DATA
// Creates Course nodes with TEACH_* and REQUIRE_* relationships
// so the learning path algorithm can find candidate courses.
// ============================================================

// ── FULL STACK DEVELOPER COURSES ───────────────────────────

CREATE (:Course {crsName: "HTML & CSS Fundamentals", crsFee: 0.0, crsTime: "20", crsRating: 4.7, crsEnroll: 52000, crsLink: "https://www.coursera.org/learn/html-css"});
CREATE (:Course {crsName: "JavaScript Essentials", crsFee: 29.99, crsTime: "35", crsRating: 4.6, crsEnroll: 41000, crsLink: "https://www.udemy.com/course/javascript-essentials"});
CREATE (:Course {crsName: "React - The Complete Guide", crsFee: 49.99, crsTime: "48", crsRating: 4.8, crsEnroll: 68000, crsLink: "https://www.udemy.com/course/react-complete-guide"});
CREATE (:Course {crsName: "Node.js Developer Course", crsFee: 39.99, crsTime: "40", crsRating: 4.5, crsEnroll: 33000, crsLink: "https://www.udemy.com/course/nodejs-developer"});
CREATE (:Course {crsName: "RESTful API Design & Development", crsFee: 29.99, crsTime: "22", crsRating: 4.4, crsEnroll: 18000, crsLink: "https://www.coursera.org/learn/restful-api"});
CREATE (:Course {crsName: "Database Systems Complete", crsFee: 39.99, crsTime: "30", crsRating: 4.5, crsEnroll: 25000, crsLink: "https://www.coursera.org/learn/database-systems"});
CREATE (:Course {crsName: "System Design Fundamentals", crsFee: 59.99, crsTime: "25", crsRating: 4.6, crsEnroll: 15000, crsLink: "https://www.educative.io/courses/system-design"});

// ── DATA SCIENCE COURSES ───────────────────────────────────

CREATE (:Course {crsName: "Python for Data Science", crsFee: 0.0, crsTime: "30", crsRating: 4.7, crsEnroll: 95000, crsLink: "https://www.coursera.org/learn/python-data-science"});
CREATE (:Course {crsName: "Statistics and Probability", crsFee: 49.99, crsTime: "28", crsRating: 4.5, crsEnroll: 30000, crsLink: "https://www.khanacademy.org/math/statistics-probability"});
CREATE (:Course {crsName: "Data Analysis with Python", crsFee: 39.99, crsTime: "32", crsRating: 4.6, crsEnroll: 42000, crsLink: "https://www.coursera.org/learn/data-analysis-python"});
CREATE (:Course {crsName: "Pandas & NumPy Masterclass", crsFee: 29.99, crsTime: "20", crsRating: 4.5, crsEnroll: 28000, crsLink: "https://www.udemy.com/course/pandas-numpy"});
CREATE (:Course {crsName: "Data Visualization with Python", crsFee: 29.99, crsTime: "18", crsRating: 4.4, crsEnroll: 22000, crsLink: "https://www.coursera.org/learn/data-visualization-python"});

// ── ML / AI COURSES ────────────────────────────────────────

CREATE (:Course {crsName: "Linear Algebra for ML", crsFee: 0.0, crsTime: "20", crsRating: 4.6, crsEnroll: 35000, crsLink: "https://www.khanacademy.org/math/linear-algebra"});
CREATE (:Course {crsName: "Probability and Statistics for ML", crsFee: 0.0, crsTime: "22", crsRating: 4.5, crsEnroll: 28000, crsLink: "https://www.coursera.org/learn/probability-ml"});
CREATE (:Course {crsName: "Machine Learning by Stanford", crsFee: 0.0, crsTime: "60", crsRating: 4.9, crsEnroll: 180000, crsLink: "https://www.coursera.org/learn/machine-learning"});
CREATE (:Course {crsName: "Deep Learning Specialization", crsFee: 49.99, crsTime: "80", crsRating: 4.8, crsEnroll: 120000, crsLink: "https://www.coursera.org/specializations/deep-learning"});
CREATE (:Course {crsName: "TensorFlow Developer Certificate", crsFee: 49.99, crsTime: "45", crsRating: 4.7, crsEnroll: 45000, crsLink: "https://www.coursera.org/professional-certificates/tensorflow"});
CREATE (:Course {crsName: "PyTorch for Deep Learning", crsFee: 39.99, crsTime: "35", crsRating: 4.6, crsEnroll: 30000, crsLink: "https://www.udemy.com/course/pytorch-deep-learning"});
CREATE (:Course {crsName: "MLOps Engineering", crsFee: 59.99, crsTime: "30", crsRating: 4.4, crsEnroll: 12000, crsLink: "https://www.coursera.org/learn/mlops"});
CREATE (:Course {crsName: "Mathematics for AI", crsFee: 29.99, crsTime: "25", crsRating: 4.5, crsEnroll: 20000, crsLink: "https://www.coursera.org/learn/math-for-ai"});
CREATE (:Course {crsName: "NLP Specialization", crsFee: 49.99, crsTime: "40", crsRating: 4.7, crsEnroll: 38000, crsLink: "https://www.coursera.org/specializations/nlp"});
CREATE (:Course {crsName: "Computer Vision with Deep Learning", crsFee: 49.99, crsTime: "35", crsRating: 4.6, crsEnroll: 25000, crsLink: "https://www.coursera.org/learn/computer-vision"});
CREATE (:Course {crsName: "AI Deployment & Production", crsFee: 39.99, crsTime: "28", crsRating: 4.3, crsEnroll: 10000, crsLink: "https://www.coursera.org/learn/ai-deployment"});

// ── BACKEND DEVELOPER COURSES ──────────────────────────────

CREATE (:Course {crsName: "Python Backend Development", crsFee: 39.99, crsTime: "40", crsRating: 4.6, crsEnroll: 35000, crsLink: "https://www.udemy.com/course/python-backend"});
CREATE (:Course {crsName: "Java Programming Masterclass", crsFee: 49.99, crsTime: "50", crsRating: 4.7, crsEnroll: 55000, crsLink: "https://www.udemy.com/course/java-masterclass"});
CREATE (:Course {crsName: "API Design and Architecture", crsFee: 29.99, crsTime: "20", crsRating: 4.5, crsEnroll: 16000, crsLink: "https://www.coursera.org/learn/api-design"});
CREATE (:Course {crsName: "Authentication & Security", crsFee: 29.99, crsTime: "18", crsRating: 4.4, crsEnroll: 14000, crsLink: "https://www.udemy.com/course/auth-security"});
CREATE (:Course {crsName: "Microservices Architecture", crsFee: 59.99, crsTime: "30", crsRating: 4.5, crsEnroll: 20000, crsLink: "https://www.udemy.com/course/microservices"});

// ── FRONTEND DEVELOPER COURSES ─────────────────────────────

CREATE (:Course {crsName: "UI/UX Design Fundamentals", crsFee: 29.99, crsTime: "22", crsRating: 4.5, crsEnroll: 30000, crsLink: "https://www.coursera.org/learn/ui-ux-design"});
CREATE (:Course {crsName: "Advanced React & State Management", crsFee: 49.99, crsTime: "35", crsRating: 4.7, crsEnroll: 28000, crsLink: "https://www.udemy.com/course/advanced-react"});
CREATE (:Course {crsName: "Web Performance Optimization", crsFee: 29.99, crsTime: "15", crsRating: 4.3, crsEnroll: 10000, crsLink: "https://www.udemy.com/course/web-performance"});

// ── DEVOPS COURSES ─────────────────────────────────────────

CREATE (:Course {crsName: "Linux Administration", crsFee: 29.99, crsTime: "30", crsRating: 4.6, crsEnroll: 40000, crsLink: "https://www.udemy.com/course/linux-admin"});
CREATE (:Course {crsName: "Docker & Containers", crsFee: 29.99, crsTime: "22", crsRating: 4.7, crsEnroll: 45000, crsLink: "https://www.udemy.com/course/docker-containers"});
CREATE (:Course {crsName: "Kubernetes Mastery", crsFee: 49.99, crsTime: "30", crsRating: 4.6, crsEnroll: 25000, crsLink: "https://www.udemy.com/course/kubernetes"});
CREATE (:Course {crsName: "Networking Fundamentals", crsFee: 0.0, crsTime: "20", crsRating: 4.4, crsEnroll: 35000, crsLink: "https://www.coursera.org/learn/networking"});
CREATE (:Course {crsName: "Cloud Platforms Overview", crsFee: 39.99, crsTime: "28", crsRating: 4.5, crsEnroll: 22000, crsLink: "https://www.coursera.org/learn/cloud-platforms"});
CREATE (:Course {crsName: "CI/CD Pipeline Mastery", crsFee: 39.99, crsTime: "20", crsRating: 4.5, crsEnroll: 15000, crsLink: "https://www.udemy.com/course/cicd-pipelines"});
CREATE (:Course {crsName: "Infrastructure Monitoring", crsFee: 29.99, crsTime: "18", crsRating: 4.3, crsEnroll: 10000, crsLink: "https://www.udemy.com/course/monitoring"});

// ── CYBERSECURITY COURSES ──────────────────────────────────

CREATE (:Course {crsName: "Operating Systems Security", crsFee: 29.99, crsTime: "25", crsRating: 4.5, crsEnroll: 18000, crsLink: "https://www.coursera.org/learn/os-security"});
CREATE (:Course {crsName: "Cryptography Fundamentals", crsFee: 0.0, crsTime: "22", crsRating: 4.6, crsEnroll: 28000, crsLink: "https://www.coursera.org/learn/cryptography"});
CREATE (:Course {crsName: "Ethical Hacking Bootcamp", crsFee: 49.99, crsTime: "45", crsRating: 4.8, crsEnroll: 55000, crsLink: "https://www.udemy.com/course/ethical-hacking"});
CREATE (:Course {crsName: "Security Tools & Penetration Testing", crsFee: 39.99, crsTime: "30", crsRating: 4.5, crsEnroll: 20000, crsLink: "https://www.udemy.com/course/security-tools"});
CREATE (:Course {crsName: "Threat Analysis & Response", crsFee: 49.99, crsTime: "25", crsRating: 4.4, crsEnroll: 12000, crsLink: "https://www.coursera.org/learn/threat-analysis"});

// ── CLOUD ENGINEER COURSES ─────────────────────────────────

CREATE (:Course {crsName: "AWS Certified Solutions Architect", crsFee: 49.99, crsTime: "45", crsRating: 4.7, crsEnroll: 70000, crsLink: "https://www.udemy.com/course/aws-solutions-architect"});
CREATE (:Course {crsName: "Microsoft Azure Fundamentals", crsFee: 0.0, crsTime: "20", crsRating: 4.5, crsEnroll: 40000, crsLink: "https://learn.microsoft.com/en-us/training/paths/az-900"});
CREATE (:Course {crsName: "Google Cloud Fundamentals", crsFee: 0.0, crsTime: "18", crsRating: 4.4, crsEnroll: 25000, crsLink: "https://www.coursera.org/learn/gcp-fundamentals"});
CREATE (:Course {crsName: "Infrastructure as Code with Terraform", crsFee: 39.99, crsTime: "25", crsRating: 4.6, crsEnroll: 18000, crsLink: "https://www.udemy.com/course/terraform-iac"});
CREATE (:Course {crsName: "Cloud Security Essentials", crsFee: 39.99, crsTime: "22", crsRating: 4.5, crsEnroll: 14000, crsLink: "https://www.coursera.org/learn/cloud-security"});

// ── MOBILE APP DEVELOPER COURSES ───────────────────────────

CREATE (:Course {crsName: "Kotlin for Android", crsFee: 39.99, crsTime: "35", crsRating: 4.6, crsEnroll: 32000, crsLink: "https://www.udemy.com/course/kotlin-android"});
CREATE (:Course {crsName: "Swift & iOS Development", crsFee: 49.99, crsTime: "40", crsRating: 4.7, crsEnroll: 38000, crsLink: "https://www.udemy.com/course/swift-ios"});
CREATE (:Course {crsName: "Flutter & Dart Complete Guide", crsFee: 49.99, crsTime: "42", crsRating: 4.8, crsEnroll: 50000, crsLink: "https://www.udemy.com/course/flutter-dart"});
CREATE (:Course {crsName: "React Native - The Practical Guide", crsFee: 49.99, crsTime: "38", crsRating: 4.6, crsEnroll: 35000, crsLink: "https://www.udemy.com/course/react-native-practical"});
CREATE (:Course {crsName: "Mobile UI Design Patterns", crsFee: 19.99, crsTime: "15", crsRating: 4.4, crsEnroll: 12000, crsLink: "https://www.udemy.com/course/mobile-ui-patterns"});
CREATE (:Course {crsName: "App Deployment & Publishing", crsFee: 19.99, crsTime: "10", crsRating: 4.3, crsEnroll: 15000, crsLink: "https://www.udemy.com/course/app-deployment"});


// ── TEACH_* RELATIONSHIPS ──────────────────────────────────
// Each course TEACHES certain skills

// HTML & CSS Fundamentals
MATCH (c:Course {crsName:"HTML & CSS Fundamentals"}), (s:ProgramingLanguage {value:"HTML"}) MERGE (c)-[:TEACH_PROGRAMINGLANGUAGE {Level:1}]->(s);
MATCH (c:Course {crsName:"HTML & CSS Fundamentals"}), (s:ProgramingLanguage {value:"CSS"}) MERGE (c)-[:TEACH_PROGRAMINGLANGUAGE {Level:1}]->(s);

// JavaScript Essentials
MATCH (c:Course {crsName:"JavaScript Essentials"}), (s:ProgramingLanguage {value:"JavaScript"}) MERGE (c)-[:TEACH_PROGRAMINGLANGUAGE {Level:2}]->(s);

// React Complete Guide
MATCH (c:Course {crsName:"React - The Complete Guide"}), (s:Framework {value:"React"}) MERGE (c)-[:TEACH_FRAMEWORK {Level:2}]->(s);
MATCH (c:Course {crsName:"React - The Complete Guide"}), (s:Knowledge {value:"State Management"}) MERGE (c)-[:TEACH_KNOWLEDGE {Level:1}]->(s);

// Node.js Developer
MATCH (c:Course {crsName:"Node.js Developer Course"}), (s:Framework {value:"Node.js"}) MERGE (c)-[:TEACH_FRAMEWORK {Level:2}]->(s);

// RESTful API
MATCH (c:Course {crsName:"RESTful API Design & Development"}), (s:Knowledge {value:"REST APIs"}) MERGE (c)-[:TEACH_KNOWLEDGE {Level:2}]->(s);
MATCH (c:Course {crsName:"RESTful API Design & Development"}), (s:Knowledge {value:"APIs"}) MERGE (c)-[:TEACH_KNOWLEDGE {Level:2}]->(s);

// Database Systems
MATCH (c:Course {crsName:"Database Systems Complete"}), (s:Knowledge {value:"Databases"}) MERGE (c)-[:TEACH_KNOWLEDGE {Level:2}]->(s);

// System Design
MATCH (c:Course {crsName:"System Design Fundamentals"}), (s:Knowledge {value:"System Design"}) MERGE (c)-[:TEACH_KNOWLEDGE {Level:3}]->(s);

// Python for Data Science
MATCH (c:Course {crsName:"Python for Data Science"}), (s:ProgramingLanguage {value:"Python"}) MERGE (c)-[:TEACH_PROGRAMINGLANGUAGE {Level:2}]->(s);
MATCH (c:Course {crsName:"Python for Data Science"}), (s:Knowledge {value:"Data Analysis"}) MERGE (c)-[:TEACH_KNOWLEDGE {Level:1}]->(s);

// Statistics
MATCH (c:Course {crsName:"Statistics and Probability"}), (s:Knowledge {value:"Statistics"}) MERGE (c)-[:TEACH_KNOWLEDGE {Level:2}]->(s);
MATCH (c:Course {crsName:"Statistics and Probability"}), (s:Knowledge {value:"Probability"}) MERGE (c)-[:TEACH_KNOWLEDGE {Level:2}]->(s);

// Data Analysis with Python
MATCH (c:Course {crsName:"Data Analysis with Python"}), (s:Knowledge {value:"Data Analysis"}) MERGE (c)-[:TEACH_KNOWLEDGE {Level:2}]->(s);

// Pandas & NumPy
MATCH (c:Course {crsName:"Pandas & NumPy Masterclass"}), (s:Tool {value:"Pandas"}) MERGE (c)-[:TEACH_TOOL {Level:2}]->(s);
MATCH (c:Course {crsName:"Pandas & NumPy Masterclass"}), (s:Tool {value:"NumPy"}) MERGE (c)-[:TEACH_TOOL {Level:2}]->(s);

// Data Visualization
MATCH (c:Course {crsName:"Data Visualization with Python"}), (s:Knowledge {value:"Data Visualization"}) MERGE (c)-[:TEACH_KNOWLEDGE {Level:2}]->(s);

// Linear Algebra
MATCH (c:Course {crsName:"Linear Algebra for ML"}), (s:Knowledge {value:"Linear Algebra"}) MERGE (c)-[:TEACH_KNOWLEDGE {Level:2}]->(s);

// Probability for ML
MATCH (c:Course {crsName:"Probability and Statistics for ML"}), (s:Knowledge {value:"Probability"}) MERGE (c)-[:TEACH_KNOWLEDGE {Level:2}]->(s);
MATCH (c:Course {crsName:"Probability and Statistics for ML"}), (s:Knowledge {value:"Statistics"}) MERGE (c)-[:TEACH_KNOWLEDGE {Level:1}]->(s);

// Machine Learning
MATCH (c:Course {crsName:"Machine Learning by Stanford"}), (s:Knowledge {value:"Machine Learning"}) MERGE (c)-[:TEACH_KNOWLEDGE {Level:3}]->(s);

// Deep Learning
MATCH (c:Course {crsName:"Deep Learning Specialization"}), (s:Knowledge {value:"Deep Learning"}) MERGE (c)-[:TEACH_KNOWLEDGE {Level:3}]->(s);

// TensorFlow
MATCH (c:Course {crsName:"TensorFlow Developer Certificate"}), (s:Framework {value:"TensorFlow"}) MERGE (c)-[:TEACH_FRAMEWORK {Level:2}]->(s);

// PyTorch
MATCH (c:Course {crsName:"PyTorch for Deep Learning"}), (s:Framework {value:"PyTorch"}) MERGE (c)-[:TEACH_FRAMEWORK {Level:2}]->(s);

// MLOps
MATCH (c:Course {crsName:"MLOps Engineering"}), (s:Knowledge {value:"MLOps"}) MERGE (c)-[:TEACH_KNOWLEDGE {Level:2}]->(s);

// Mathematics for AI
MATCH (c:Course {crsName:"Mathematics for AI"}), (s:Knowledge {value:"Mathematics"}) MERGE (c)-[:TEACH_KNOWLEDGE {Level:2}]->(s);
MATCH (c:Course {crsName:"Mathematics for AI"}), (s:Knowledge {value:"Linear Algebra"}) MERGE (c)-[:TEACH_KNOWLEDGE {Level:1}]->(s);

// NLP
MATCH (c:Course {crsName:"NLP Specialization"}), (s:Knowledge {value:"NLP"}) MERGE (c)-[:TEACH_KNOWLEDGE {Level:2}]->(s);

// Computer Vision
MATCH (c:Course {crsName:"Computer Vision with Deep Learning"}), (s:Knowledge {value:"Computer Vision"}) MERGE (c)-[:TEACH_KNOWLEDGE {Level:2}]->(s);

// AI Deployment
MATCH (c:Course {crsName:"AI Deployment & Production"}), (s:Knowledge {value:"AI Deployment"}) MERGE (c)-[:TEACH_KNOWLEDGE {Level:3}]->(s);

// Python Backend
MATCH (c:Course {crsName:"Python Backend Development"}), (s:ProgramingLanguage {value:"Python"}) MERGE (c)-[:TEACH_PROGRAMINGLANGUAGE {Level:2}]->(s);
MATCH (c:Course {crsName:"Python Backend Development"}), (s:Knowledge {value:"APIs"}) MERGE (c)-[:TEACH_KNOWLEDGE {Level:1}]->(s);

// Java Masterclass
MATCH (c:Course {crsName:"Java Programming Masterclass"}), (s:ProgramingLanguage {value:"Java"}) MERGE (c)-[:TEACH_PROGRAMINGLANGUAGE {Level:2}]->(s);

// API Design
MATCH (c:Course {crsName:"API Design and Architecture"}), (s:Knowledge {value:"APIs"}) MERGE (c)-[:TEACH_KNOWLEDGE {Level:2}]->(s);
MATCH (c:Course {crsName:"API Design and Architecture"}), (s:Knowledge {value:"REST APIs"}) MERGE (c)-[:TEACH_KNOWLEDGE {Level:1}]->(s);

// Authentication
MATCH (c:Course {crsName:"Authentication & Security"}), (s:Knowledge {value:"Authentication"}) MERGE (c)-[:TEACH_KNOWLEDGE {Level:2}]->(s);

// Microservices
MATCH (c:Course {crsName:"Microservices Architecture"}), (s:Knowledge {value:"Microservices"}) MERGE (c)-[:TEACH_KNOWLEDGE {Level:3}]->(s);
MATCH (c:Course {crsName:"Microservices Architecture"}), (s:Knowledge {value:"System Design"}) MERGE (c)-[:TEACH_KNOWLEDGE {Level:2}]->(s);

// UI/UX
MATCH (c:Course {crsName:"UI/UX Design Fundamentals"}), (s:Knowledge {value:"UI/UX"}) MERGE (c)-[:TEACH_KNOWLEDGE {Level:2}]->(s);

// Advanced React
MATCH (c:Course {crsName:"Advanced React & State Management"}), (s:Knowledge {value:"State Management"}) MERGE (c)-[:TEACH_KNOWLEDGE {Level:2}]->(s);
MATCH (c:Course {crsName:"Advanced React & State Management"}), (s:Framework {value:"React"}) MERGE (c)-[:TEACH_FRAMEWORK {Level:3}]->(s);

// Web Performance
MATCH (c:Course {crsName:"Web Performance Optimization"}), (s:Knowledge {value:"Web Performance"}) MERGE (c)-[:TEACH_KNOWLEDGE {Level:2}]->(s);

// Linux
MATCH (c:Course {crsName:"Linux Administration"}), (s:Tool {value:"Linux"}) MERGE (c)-[:TEACH_TOOL {Level:2}]->(s);

// Docker
MATCH (c:Course {crsName:"Docker & Containers"}), (s:Tool {value:"Docker"}) MERGE (c)-[:TEACH_TOOL {Level:2}]->(s);
MATCH (c:Course {crsName:"Docker & Containers"}), (s:Tool {value:"Containers"}) MERGE (c)-[:TEACH_TOOL {Level:2}]->(s);

// Kubernetes
MATCH (c:Course {crsName:"Kubernetes Mastery"}), (s:Tool {value:"Kubernetes"}) MERGE (c)-[:TEACH_TOOL {Level:3}]->(s);

// Networking
MATCH (c:Course {crsName:"Networking Fundamentals"}), (s:Knowledge {value:"Networking"}) MERGE (c)-[:TEACH_KNOWLEDGE {Level:2}]->(s);

// Cloud Platforms
MATCH (c:Course {crsName:"Cloud Platforms Overview"}), (s:Platform {value:"Cloud Platforms"}) MERGE (c)-[:TEACH_PLATFORM {Level:2}]->(s);

// CI/CD
MATCH (c:Course {crsName:"CI/CD Pipeline Mastery"}), (s:Tool {value:"CI/CD"}) MERGE (c)-[:TEACH_TOOL {Level:2}]->(s);

// Monitoring
MATCH (c:Course {crsName:"Infrastructure Monitoring"}), (s:Tool {value:"Monitoring"}) MERGE (c)-[:TEACH_TOOL {Level:2}]->(s);

// OS Security
MATCH (c:Course {crsName:"Operating Systems Security"}), (s:Knowledge {value:"Operating Systems"}) MERGE (c)-[:TEACH_KNOWLEDGE {Level:2}]->(s);

// Cryptography
MATCH (c:Course {crsName:"Cryptography Fundamentals"}), (s:Knowledge {value:"Cryptography"}) MERGE (c)-[:TEACH_KNOWLEDGE {Level:2}]->(s);

// Ethical Hacking
MATCH (c:Course {crsName:"Ethical Hacking Bootcamp"}), (s:Knowledge {value:"Ethical Hacking"}) MERGE (c)-[:TEACH_KNOWLEDGE {Level:3}]->(s);

// Security Tools
MATCH (c:Course {crsName:"Security Tools & Penetration Testing"}), (s:Tool {value:"Security Tools"}) MERGE (c)-[:TEACH_TOOL {Level:2}]->(s);

// Threat Analysis
MATCH (c:Course {crsName:"Threat Analysis & Response"}), (s:Knowledge {value:"Threat Analysis"}) MERGE (c)-[:TEACH_KNOWLEDGE {Level:3}]->(s);

// AWS
MATCH (c:Course {crsName:"AWS Certified Solutions Architect"}), (s:Platform {value:"AWS"}) MERGE (c)-[:TEACH_PLATFORM {Level:2}]->(s);
MATCH (c:Course {crsName:"AWS Certified Solutions Architect"}), (s:Platform {value:"Cloud Platforms"}) MERGE (c)-[:TEACH_PLATFORM {Level:1}]->(s);

// Azure
MATCH (c:Course {crsName:"Microsoft Azure Fundamentals"}), (s:Platform {value:"Azure"}) MERGE (c)-[:TEACH_PLATFORM {Level:2}]->(s);

// GCP
MATCH (c:Course {crsName:"Google Cloud Fundamentals"}), (s:Platform {value:"GCP"}) MERGE (c)-[:TEACH_PLATFORM {Level:2}]->(s);

// IaC
MATCH (c:Course {crsName:"Infrastructure as Code with Terraform"}), (s:Knowledge {value:"Infrastructure as Code"}) MERGE (c)-[:TEACH_KNOWLEDGE {Level:2}]->(s);

// Cloud Security
MATCH (c:Course {crsName:"Cloud Security Essentials"}), (s:Knowledge {value:"Cloud Security"}) MERGE (c)-[:TEACH_KNOWLEDGE {Level:3}]->(s);

// Kotlin
MATCH (c:Course {crsName:"Kotlin for Android"}), (s:ProgramingLanguage {value:"Kotlin"}) MERGE (c)-[:TEACH_PROGRAMINGLANGUAGE {Level:2}]->(s);

// Swift & iOS
MATCH (c:Course {crsName:"Swift & iOS Development"}), (s:ProgramingLanguage {value:"Swift"}) MERGE (c)-[:TEACH_PROGRAMINGLANGUAGE {Level:2}]->(s);
MATCH (c:Course {crsName:"Swift & iOS Development"}), (s:Knowledge {value:"Mobile UI"}) MERGE (c)-[:TEACH_KNOWLEDGE {Level:1}]->(s);

// Flutter
MATCH (c:Course {crsName:"Flutter & Dart Complete Guide"}), (s:Framework {value:"Flutter"}) MERGE (c)-[:TEACH_FRAMEWORK {Level:2}]->(s);

// React Native
MATCH (c:Course {crsName:"React Native - The Practical Guide"}), (s:Framework {value:"React Native"}) MERGE (c)-[:TEACH_FRAMEWORK {Level:2}]->(s);

// Mobile UI
MATCH (c:Course {crsName:"Mobile UI Design Patterns"}), (s:Knowledge {value:"Mobile UI"}) MERGE (c)-[:TEACH_KNOWLEDGE {Level:2}]->(s);

// App Deployment
MATCH (c:Course {crsName:"App Deployment & Publishing"}), (s:Knowledge {value:"App Deployment"}) MERGE (c)-[:TEACH_KNOWLEDGE {Level:2}]->(s);


// ── REQUIRE_* RELATIONSHIPS ────────────────────────────────
// Prerequisites for courses (what you need before taking the course)

// JavaScript requires HTML & CSS
MATCH (c:Course {crsName:"JavaScript Essentials"}), (s:ProgramingLanguage {value:"HTML"}) MERGE (c)-[:REQUIRE_PROGRAMINGLANGUAGE {Level:1}]->(s);
MATCH (c:Course {crsName:"JavaScript Essentials"}), (s:ProgramingLanguage {value:"CSS"}) MERGE (c)-[:REQUIRE_PROGRAMINGLANGUAGE {Level:1}]->(s);

// React requires JavaScript
MATCH (c:Course {crsName:"React - The Complete Guide"}), (s:ProgramingLanguage {value:"JavaScript"}) MERGE (c)-[:REQUIRE_PROGRAMINGLANGUAGE {Level:1}]->(s);

// Node.js requires JavaScript
MATCH (c:Course {crsName:"Node.js Developer Course"}), (s:ProgramingLanguage {value:"JavaScript"}) MERGE (c)-[:REQUIRE_PROGRAMINGLANGUAGE {Level:1}]->(s);

// REST API requires Node.js
MATCH (c:Course {crsName:"RESTful API Design & Development"}), (s:Framework {value:"Node.js"}) MERGE (c)-[:REQUIRE_FRAMEWORK {Level:1}]->(s);

// Database requires REST APIs knowledge
MATCH (c:Course {crsName:"Database Systems Complete"}), (s:Knowledge {value:"APIs"}) MERGE (c)-[:REQUIRE_KNOWLEDGE {Level:1}]->(s);

// System Design requires Databases
MATCH (c:Course {crsName:"System Design Fundamentals"}), (s:Knowledge {value:"Databases"}) MERGE (c)-[:REQUIRE_KNOWLEDGE {Level:1}]->(s);

// Data Analysis requires Python
MATCH (c:Course {crsName:"Data Analysis with Python"}), (s:ProgramingLanguage {value:"Python"}) MERGE (c)-[:REQUIRE_PROGRAMINGLANGUAGE {Level:1}]->(s);

// Pandas requires Data Analysis
MATCH (c:Course {crsName:"Pandas & NumPy Masterclass"}), (s:Knowledge {value:"Data Analysis"}) MERGE (c)-[:REQUIRE_KNOWLEDGE {Level:1}]->(s);

// Data Viz requires Data Analysis
MATCH (c:Course {crsName:"Data Visualization with Python"}), (s:Knowledge {value:"Data Analysis"}) MERGE (c)-[:REQUIRE_KNOWLEDGE {Level:1}]->(s);

// ML requires Python and Statistics
MATCH (c:Course {crsName:"Machine Learning by Stanford"}), (s:ProgramingLanguage {value:"Python"}) MERGE (c)-[:REQUIRE_PROGRAMINGLANGUAGE {Level:1}]->(s);
MATCH (c:Course {crsName:"Machine Learning by Stanford"}), (s:Knowledge {value:"Statistics"}) MERGE (c)-[:REQUIRE_KNOWLEDGE {Level:1}]->(s);

// Deep Learning requires ML
MATCH (c:Course {crsName:"Deep Learning Specialization"}), (s:Knowledge {value:"Machine Learning"}) MERGE (c)-[:REQUIRE_KNOWLEDGE {Level:2}]->(s);

// TensorFlow requires Deep Learning
MATCH (c:Course {crsName:"TensorFlow Developer Certificate"}), (s:Knowledge {value:"Deep Learning"}) MERGE (c)-[:REQUIRE_KNOWLEDGE {Level:2}]->(s);

// PyTorch requires Deep Learning
MATCH (c:Course {crsName:"PyTorch for Deep Learning"}), (s:Knowledge {value:"Deep Learning"}) MERGE (c)-[:REQUIRE_KNOWLEDGE {Level:2}]->(s);

// MLOps requires TensorFlow or ML
MATCH (c:Course {crsName:"MLOps Engineering"}), (s:Knowledge {value:"Machine Learning"}) MERGE (c)-[:REQUIRE_KNOWLEDGE {Level:2}]->(s);

// NLP requires Deep Learning
MATCH (c:Course {crsName:"NLP Specialization"}), (s:Knowledge {value:"Deep Learning"}) MERGE (c)-[:REQUIRE_KNOWLEDGE {Level:2}]->(s);

// Computer Vision requires Deep Learning
MATCH (c:Course {crsName:"Computer Vision with Deep Learning"}), (s:Knowledge {value:"Deep Learning"}) MERGE (c)-[:REQUIRE_KNOWLEDGE {Level:2}]->(s);

// AI Deployment requires ML
MATCH (c:Course {crsName:"AI Deployment & Production"}), (s:Knowledge {value:"Machine Learning"}) MERGE (c)-[:REQUIRE_KNOWLEDGE {Level:2}]->(s);

// API Design requires Python or Java
MATCH (c:Course {crsName:"API Design and Architecture"}), (s:ProgramingLanguage {value:"Python"}) MERGE (c)-[:REQUIRE_PROGRAMINGLANGUAGE {Level:1}]->(s);

// Auth requires API knowledge
MATCH (c:Course {crsName:"Authentication & Security"}), (s:Knowledge {value:"APIs"}) MERGE (c)-[:REQUIRE_KNOWLEDGE {Level:1}]->(s);

// Microservices requires System Design
MATCH (c:Course {crsName:"Microservices Architecture"}), (s:Knowledge {value:"System Design"}) MERGE (c)-[:REQUIRE_KNOWLEDGE {Level:1}]->(s);

// Advanced React requires React
MATCH (c:Course {crsName:"Advanced React & State Management"}), (s:Framework {value:"React"}) MERGE (c)-[:REQUIRE_FRAMEWORK {Level:1}]->(s);

// Web Performance requires UI/UX
MATCH (c:Course {crsName:"Web Performance Optimization"}), (s:Knowledge {value:"UI/UX"}) MERGE (c)-[:REQUIRE_KNOWLEDGE {Level:1}]->(s);

// Docker requires Linux
MATCH (c:Course {crsName:"Docker & Containers"}), (s:Tool {value:"Linux"}) MERGE (c)-[:REQUIRE_TOOL {Level:1}]->(s);

// Kubernetes requires Docker
MATCH (c:Course {crsName:"Kubernetes Mastery"}), (s:Tool {value:"Docker"}) MERGE (c)-[:REQUIRE_TOOL {Level:1}]->(s);

// Cloud Platforms requires Networking
MATCH (c:Course {crsName:"Cloud Platforms Overview"}), (s:Knowledge {value:"Networking"}) MERGE (c)-[:REQUIRE_KNOWLEDGE {Level:1}]->(s);

// CI/CD requires Cloud Platforms
MATCH (c:Course {crsName:"CI/CD Pipeline Mastery"}), (s:Platform {value:"Cloud Platforms"}) MERGE (c)-[:REQUIRE_PLATFORM {Level:1}]->(s);

// Monitoring requires CI/CD
MATCH (c:Course {crsName:"Infrastructure Monitoring"}), (s:Tool {value:"CI/CD"}) MERGE (c)-[:REQUIRE_TOOL {Level:1}]->(s);

// OS Security requires Networking
MATCH (c:Course {crsName:"Operating Systems Security"}), (s:Knowledge {value:"Networking"}) MERGE (c)-[:REQUIRE_KNOWLEDGE {Level:1}]->(s);

// Ethical Hacking requires Cryptography
MATCH (c:Course {crsName:"Ethical Hacking Bootcamp"}), (s:Knowledge {value:"Cryptography"}) MERGE (c)-[:REQUIRE_KNOWLEDGE {Level:1}]->(s);

// Security Tools requires OS
MATCH (c:Course {crsName:"Security Tools & Penetration Testing"}), (s:Knowledge {value:"Operating Systems"}) MERGE (c)-[:REQUIRE_KNOWLEDGE {Level:1}]->(s);

// Threat Analysis requires Ethical Hacking
MATCH (c:Course {crsName:"Threat Analysis & Response"}), (s:Knowledge {value:"Ethical Hacking"}) MERGE (c)-[:REQUIRE_KNOWLEDGE {Level:2}]->(s);

// IaC requires Containers
MATCH (c:Course {crsName:"Infrastructure as Code with Terraform"}), (s:Tool {value:"Containers"}) MERGE (c)-[:REQUIRE_TOOL {Level:1}]->(s);

// Cloud Security requires IaC
MATCH (c:Course {crsName:"Cloud Security Essentials"}), (s:Knowledge {value:"Infrastructure as Code"}) MERGE (c)-[:REQUIRE_KNOWLEDGE {Level:1}]->(s);

// Kotlin requires Java
MATCH (c:Course {crsName:"Kotlin for Android"}), (s:ProgramingLanguage {value:"Java"}) MERGE (c)-[:REQUIRE_PROGRAMINGLANGUAGE {Level:1}]->(s);

// Flutter requires Mobile UI
MATCH (c:Course {crsName:"Flutter & Dart Complete Guide"}), (s:Knowledge {value:"Mobile UI"}) MERGE (c)-[:REQUIRE_KNOWLEDGE {Level:1}]->(s);

// React Native requires JavaScript and Mobile UI
MATCH (c:Course {crsName:"React Native - The Practical Guide"}), (s:ProgramingLanguage {value:"JavaScript"}) MERGE (c)-[:REQUIRE_PROGRAMINGLANGUAGE {Level:1}]->(s);
MATCH (c:Course {crsName:"React Native - The Practical Guide"}), (s:Knowledge {value:"Mobile UI"}) MERGE (c)-[:REQUIRE_KNOWLEDGE {Level:1}]->(s);

// App Deployment requires APIs
MATCH (c:Course {crsName:"App Deployment & Publishing"}), (s:Knowledge {value:"APIs"}) MERGE (c)-[:REQUIRE_KNOWLEDGE {Level:1}]->(s);
