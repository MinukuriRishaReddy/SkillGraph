## 🎓 Skill Graph
Learning Path Recommendation System using Skill Graph and Graph Databases

![React](https://img.shields.io/badge/Frontend-React-blue)
![Django](https://img.shields.io/badge/Backend-Django-green)
![Neo4j](https://img.shields.io/badge/Database-Neo4j-brightgreen)
![Python](https://img.shields.io/badge/Python-3.10+-yellow)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-Academic-orange)

## 🌐 Live Demo

🔗 **https://skill-graph-nu.vercel.app**

---

## 📖 Overview

The Learning Path Recommendation System is an intelligent educational platform that generates personalized learning roadmaps based on a learner's existing skills and desired career goals.

Traditional learning platforms recommend standalone courses without considering prerequisite relationships among skills. This project addresses that limitation by leveraging Skill Graphs, Neo4j Graph Databases, and Graph Traversal Algorithms to provide structured, career-oriented learning paths.

The system identifies missing skills, analyzes dependencies, and generates an optimized learning roadmap that guides users from their current knowledge level to their target career.

---

## ✨ Features

### 🎯 Personalized Learning Paths
- Generates customized learning roadmaps.
- Adapts recommendations based on user skills and career goals.
- Provides structured progression from beginner to advanced concepts.

### 🔍 Skill Gap Analysis
- Compares current skills with required career skills.
- Identifies missing competencies.
- Focuses learning on relevant skill gaps.

### 🌐 Skill Graph Representation
- Skills represented as graph nodes.
- Dependencies represented as directed edges.
- Maintains prerequisite relationships between technologies.

### ⚡ Graph-Based Recommendation Engine
- Breadth First Search (BFS)
- Topological Sorting
- Similarity Analysis
- Learning Path Optimization

### 🗄 Neo4j Graph Database
- Stores skills, careers, courses, and relationships.
- Enables efficient graph traversal and querying.
- Supports scalable recommendation generation.

### 📚 Course Recommendation System
- Maps skills to relevant courses.
- Suggests learning resources for each skill.
- Generates complete learning roadmaps.

### 📊 Interactive Visualization
- Displays skill relationships visually.
- Helps learners understand learning dependencies.
- Provides graph-based exploration of career paths.

### 👤 User Management
- User Registration
- Login System
- Career Objective Tracking
- Learning Progress Personalization

---

## 🏗 System Architecture

```text
User
 │
 ▼
Frontend (React + Vite)
 │
 ▼
REST APIs (Django)
 │
 ▼
Recommendation Engine
 ├── Skill Gap Analysis
 ├── Graph Traversal
 ├── Learning Path Generation
 └── Course Recommendation
 │
 ▼
Neo4j Graph Database
 ├── Skills
 ├── Careers
 ├── Courses
 └── Relationships
```

---

## 🛠 Technology Stack

### Frontend
- React.js
- Vite
- Material UI (MUI)
- React Router DOM
- Axios
- XYFlow React

### Backend
- Python
- Django
- Django REST Framework
- Django CORS Headers

### Database
- Neo4j Graph Database
- Neomodel
- Py2neo

### Data Processing
- Pandas
- NumPy

### Algorithms
- Breadth First Search (BFS)
- Topological Sorting
- Graph Traversal
- Similarity Matching
- Learning Path Optimization

### Development Tools
- Git
- GitHub
- VS Code
- Neo4j Desktop

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/MinukuriRishaReddy/SkillGraph.git

cd SkillGraph
```

### Create Virtual Environment

#### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

#### Linux / Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Neo4j

Create a `.env` file:

```env
SCHEME=bolt://
URL=localhost:7687
NEO4J_USER=neo4j
PASSWORD=your_password
```

### Run Backend

```bash
python manage.py runserver
```

### Run Frontend

```bash
cd frontend

npm install

npm run dev
```

---

## 📡 API Endpoints

| Endpoint | Method | Description |
|-----------|---------|-------------|
| `/apis/career/` | GET | Get all careers |
| `/apis/career/one?id=<id>` | GET | Get career by ID |
| `/apis/career/lo?id=<id>` | GET | Get learning objects needed for career |
| `/apis/lo/language/` | GET | Get all programming languages |
| `/apis/lo/knowledge` | GET | Get all knowledge learning objects |
| `/apis/lo/tool` | GET | Get all tool learning objects |
| `/apis/lo/platform` | GET | Get all platform learning objects |
| `/apis/lo/framework` | GET | Get all framework learning objects |
| `/apis/course?id=<id>` | GET | Get course information |
| `/apis/course/provided/lo?id=<id>` | GET | Get learning objects provided by a course |
| `/apis/course/required/lo?id=<id>` | GET | Get prerequisite learning objects required by a course |
| `/apis/user/login?email=<email>` | GET | Login user using email |
| `/apis/user/register` | POST | Register user `{name, email}` |
| `/apis/user/info/?id=<id>` | GET | Get user profile information |
| `/apis/user/create` | POST | Create user profile `{id, cost, time}` |
| `/apis/user/objective` | POST | Set career objective `{user_id, career_id}` |
| `/apis/user/has` | POST | Add user skills `{user_id, list_lo}` |
| `/apis/user/need?id=<id>` | GET | Get learning objects required by user |
| `/apis/user/learning-path?id=<id>` | GET | Generate personalized learning path |
| `/admin/` | GET | Django Admin Panel |

---

## 📂 Project Structure

```text
Learning-Path-Recommendation-System/
│
├── RecommendationSystem/      # Django settings & URLs
├── apis/                      # API views & URL routing
├── models/                    # Neo4j models & connection
├── services/                  # Business logic layer
├── algorithm_implementation/  # Learning path algorithm v1
├── algorithm_v2/              # Learning path algorithm v2
├── constants/                 # Algorithm constants
├── utilities/                 # Cypher query builders
├── static/                    # Generated learning path visualizations
├── manage.py                  # Django management script
├── requirements.txt           # Python dependencies
└── .env                       # Environment variables
```

---

## 🔄 Workflow

1. User registers and logs into the platform.
2. User selects a target career path.
3. User provides existing skills.
4. System performs skill gap analysis.
5. Neo4j graph is traversed to identify missing skills.
6. Recommendation engine generates an optimized learning path.
7. Relevant courses and learning resources are mapped.
8. Personalized roadmap is displayed to the user.

---

## 🎯 Applications

- Career Guidance Platforms
- Online Learning Systems
- Educational Recommendation Systems
- Professional Upskilling Platforms
- Personalized Learning Environments
- Skill Development Programs

---

## 🔮 Future Enhancements

- AI-Powered Adaptive Recommendations
- Real-Time Industry Skill Analysis
- LinkedIn Integration
- Resume Skill Matching
- Progress Tracking Dashboard
- Certification Recommendations
- Job Recommendation Engine
- LLM-Based Career Assistant
- Multi-Career Path Recommendations

---

## 📈 Benefits

- Structured learning progression
- Reduced course-selection confusion
- Personalized recommendations
- Efficient skill acquisition
- Career-focused learning guidance
- Improved learner engagement

---

## 👨‍💻 Author

**Minukuri Risha Reddy**

B.Tech Computer Science and Engineering  
Anurag University, Hyderabad

### Areas of Interest
- Artificial Intelligence
- Machine Learning
- Graph Databases
- Blockchain Technology
- Full Stack Development
- Data Analytics

---

## 📜 License

This project was developed for academic and research purposes.

Feel free to use, extend, and improve the project with proper attribution.

---

## ⭐ Support

If you found this project useful, consider giving it a Star ⭐ on GitHub.

### Live Demo
🔗 https://skill-graph-nu.vercel.app
