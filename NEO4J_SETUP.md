# Neo4j Desktop Setup Guide

## 1. Download & Install Neo4j Desktop
1. Go to → https://neo4j.com/download/
2. Download **Neo4j Desktop** for Windows
3. Install and launch it

---

## 2. Create a New Project & Database

1. Open **Neo4j Desktop**
2. Click **"New Project"** → give it a name (e.g. `LearningPath`)
3. Inside the project, click **"Add"** → **"Local DBMS"**
4. Fill in the form:
   - **Name:** `LearningPathDB`
   - **Password:** `neo4jpass`  *(must match your `.env` file)*
   - **Version:** Select `4.4.x` (recommended for this project)
5. Click **"Create"**

---

## 3. Start the Database

1. Click the **▶ Start** button next to your database
2. Wait until the status shows **🟢 Active**
3. The database is now running on:
   - **Bolt:** `bolt://localhost:7687`
   - **Browser:** `http://localhost:7474`

---

## 4. Configure `.env` File

Make sure your `.env` file in the project root matches your Neo4j credentials:

```env
SCHEME=bolt://
URL=localhost:7687
NEO4J_USER=neo4j
USERNAMEE=neo4j
PASSWORD=neo4jpass
```

> ⚠️ The `PASSWORD` must exactly match what you set in Step 2.

---

## 5. Verify Connection in Neo4j Browser

1. In Neo4j Desktop, click **"Open"** → **"Neo4j Browser"**
2. Login with:
   - **Username:** `neo4j`
   - **Password:** `neo4jpass`
3. Run this query to verify:
   ```cypher
   RETURN "Connected!" AS status
   ```

---

## 6. Install Required Neo4j Plugins (Optional but Recommended)

Some algorithm features use **Graph Data Science (GDS)**:

1. In Neo4j Desktop, click your database → **"Plugins"** tab
2. Install **"Graph Data Science Library"** → click **Install**
3. Restart the database

---

## 7. Run the Django Project

Once Neo4j is active, run the Django server:

```powershell
# In project root (PowerShell)
.\venv\Scripts\activate
python manage.py runserver
```

Visit → **http://127.0.0.1:8000/**

---

## 8. Quick Troubleshooting

| Problem | Fix |
|---------|-----|
| `Failed to establish connection` | Neo4j is not started — click ▶ Start in Desktop |
| `Authentication failure` | Password in `.env` doesn't match Neo4j Desktop password |
| `ServiceUnavailable` | Check that Bolt port `7687` is not blocked by firewall |
| `Database not found` | Make sure the database status is 🟢 Active, not just installed |

---

## 9. Default Ports

| Service | Port | URL |
|---------|------|-----|
| **Bolt (API)** | `7687` | `bolt://localhost:7687` |
| **HTTP Browser** | `7474` | `http://localhost:7474` |
| **HTTPS** | `7473` | `https://localhost:7473` |
