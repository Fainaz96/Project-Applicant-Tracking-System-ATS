# 📘 **Complete Product Document – AI-Powered ATS (Gemini A2A Multi-Agent Architecture)**

---

# 1. **Product Overview**

The **AI-Powered Applicant Tracking System (ATS)** automates the end-to-end resume screening process using a **multi-agent AI framework powered by Gemini A2A**.

This system:

* Reads uploaded resumes
* Parses candidate information
* Extracts skills automatically
* Generates embeddings for similarity ranking
* Matches candidates to job criteria
* Produces a final AI-ranked candidate list

It is designed to be:

* **Free-tier friendly**
* **Modular**
* **Scalable**
* **Easy to deploy**
* **Showcase-ready for interviews**

---

# 2. **Target Users**

### 👨‍💼 **Recruiters / HR Teams**

Need automated resume screening and quick ranking.

### 🧑‍🤝‍🧑 **Hiring Managers**

Need structured candidate insights.

### 🧑‍💻 **AI/ML Engineering Teams**

Need a robust, agentic AI architecture.

---

# 3. **Key Features**

## ✔ 1. Resume Upload

Recruiter uploads PDF/DOCX resumes.

## ✔ 2. Parsing Agent (Gemini A2A)

Extracts:

* Name
* Email
* Phone
* Experience summary
* Skills
* Education
* Certifications

## ✔ 3. Skill Extraction Agent

Identifies:

* Tech skills
* Soft skills
* Tools & frameworks
* Clusters and tags

## ✔ 4. Embeddings & Vector DB (Chroma)

Converts text → embeddings → stores in ChromaDB.

Supports:

* Semantic search
* Similarity ranking
* Job-candidate matching

## ✔ 5. Ranking Agent

Combines:

* Skill match score
* Experience weight
* Embedding similarity
* AI-generated explanations

## ✔ 6. Dashboard UI

Recruiter sees:

* Ranked candidates
* Scores
* Reasoning
* Skill insights

---

# 4. **System Architecture (Gemini A2A Multi-Agent Model)**

Architecture contains:

* Django Frontend
* Django Backend API
* Gemini Orchestrator
* Three Gemini Sub-Agents
* Chroma Vector DB
* PostgreSQL Database
* File Storage

---

## 🧩 Architecture Components (Tamil + English Mix)

### 1️⃣ **Django Frontend**

Simple UI using Django templates:

* Upload CV
* View applicants
* View ranking
* Candidate details

### 2️⃣ **Django Backend**

Handles:

* File upload
* Call Orchestrator Agent
* Save results in DB
* Serve UI data

---

# 🤖 3️⃣ **Gemini A2A Multi-Agent Layer**

### **🌐 Orchestrator Agent (Master Agent)**

Controls the entire pipeline:

1. Trigger Parsing Agent
2. Trigger Skill Agent
3. Generate embeddings
4. Query vector DB
5. Trigger Ranking Agent
6. Send result to Django backend

---

## **🤖 Agent 1: Resume Parsing Agent**

Role:

* Extract structured information
* Clean & normalize text
* Produce JSON output

Example output:

```
{
  "name": "John Doe",
  "email": "john@gmail.com",
  "experience": "3 years in Python & ML",
  "skills_raw": "Python, ML, TensorFlow"
}
```

---

## **🤖 Agent 2: Skill Extraction Agent**

Role:

* Extract skill sets
* Categorize skills
* Provide confidence scores
* Create structured skill profile

Example:

```
{
  "tech_skills": ["Python", "Django", "ML"],
  "soft_skills": ["Teamwork"],
  "confidence": 0.92
}
```

---

## **🤖 Agent 3: Ranking Agent**

Role:

* Compare applicants vs job description
* Consider embeddings & skill score
* Provide final ranking

Example:

```
{
  "total_score": 89,
  "skill_score": 94,
  "experience_score": 82,
  "reason": "Strong Python + ML background"
}
```

---

# 🧠 4️⃣ **ChromaDB (Vector Database)**

Stores:

* Embeddings
* Candidate vectors
* Resume semantic fingerprints

Allows **similarity search**.

Also 100% free + offline compatible.

---

# 5️⃣ **PostgreSQL Database**

Stores structured data:

* Applicant details
* Skills
* AI scoring
* Resume paths
* Timestamps

Postgres free tier available (Railway, Supabase).

---

# 6️⃣ **Local File Storage**

Resume PDFs stored in:

```
/media/resumes/
```

No cost, easy to manage.

---

# 5. **End-to-End Workflow**

### **Step 1:** Recruiter uploads resume

### **Step 2:** Django backend stores file → calls Orchestrator

### **Step 3:** Orchestrator → Parsing Agent

### **Step 4:** Parsed JSON generated

### **Step 5:** Orchestrator → Skill Agent

### **Step 6:** Skill extraction completed

### **Step 7:** Embeddings generated & saved in Chroma

### **Step 8:** Ranking Agent produces final score

### **Step 9:** Results saved to PostgreSQL

### **Step 10:** Recruiter views ranked applicants in UI

This pipeline is clean, modular, and production-ready.

---

# 6. **Database Schema (ERD)**

### **Applicants**

* id
* name
* email
* phone
* experience_summary
* parsed_data (JSON)
* resume_path
* created_at

### **Skills**

* id
* name

### **ApplicantSkills**

* id
* applicant_id
* skill_id
* confidence

### **Evaluations**

* applicant_id
* total_score
* skill_score
* experience_score
* reason

### **Embeddings**

* applicant_id
* vector_data

---

# 7. **Tech Stack**

### **Backend**

* Django (free)
* Python
* Gemini A2A Agents
* ChromaDB
* PostgreSQL

### **Frontend**

* Django Templates
* HTML/CSS

### **AI**

* Gemini Flash / Pro Mix (free-tier friendly)
* Embedding models
* NLP pipelines

---

# 8. **Why This Architecture is Ideal for Take-Home Assignment**

✔ Uses latest **Gemini agentic AI**
✔ Fully modular multi-agent system
✔ Runs on **free-tier tools**
✔ Clean Django-based implementation
✔ Demonstrates strong AI engineering skills
✔ Recruiters easily understand the output
✔ Very modern design (2025 expectation)

This architecture will **impress interviewers** immediately.

---

# 9. **Future Enhancements**

* Multi-job matching
* JD → auto skill extraction
* Multi-agent negotiation (A2A advanced)
* Chat-based candidate insight
* Admin panel for HR
* Automated shortlisting emails
* Full analytics dashboard

---

# 10. **Conclusion**

This ATS product is a **powerful, modern, AI-driven system** built using **Gemini A2A multi-agent architecture**, suitable for real hiring pipelines and ideal as a demonstration of your engineering capability.

It shows mastery in:

* Django
* AI agents
* System design
* Vector search
* LLM orchestration
* End-to-end application architecture


