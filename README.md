# 🚀 AI-Powered Applicant Tracking System (ATS)

An intelligent recruitment platform that leverages Google's Gemini AI to automate resume screening, parsing, skill extraction, and candidate ranking. This system helps recruiters save time by instantly identifying the best candidates for specific job roles.

---

## 🌟 Key Features

*   **🤖 AI Resume Parsing**: Automatically extracts candidate details (Name, Email, Phone, Experience) from PDF and DOCX resumes using Gemini 1.5 Flash.
*   **🎯 Context-Aware Ranking**: ranks candidates specifically against the **Job Description** they applied for, providing a relevance score (0-100%).
*   **💼 Job Board & Career Page**: A public-facing career page where candidates can browse open positions and apply directly.
*   **🧠 Skill Extraction**: Identifies technical and soft skills and saves them to the database.
*   **🔍 Vector Search**: Uses **ChromaDB** for semantic search capabilities, allowing purely conceptual matching between candidates and jobs.
*   **📊 Recruiter Dashboard**: A centralized view to manage applicants, view AI evaluations, and sort candidates by best fit.

---

## 🛠️ Tech Stack

*   **Backend**: Django 5.0 (Python)
*   **AI Model**: Google Gemini 2.5 Flash / Flash Lite (via `google-generativeai`)
*   **Vector Database**: ChromaDB (for embeddings and semantic search)
*   **Database**: SQLite (Development) / PostgreSQL (Production ready)
*   **Frontend**: HTML5, CSS3, Django Templates
*   **PDF Processing**: `pypdf`
*   **Word Processing**: `docx2txt`

---

## ⚙️ Installation & Setup

### Prerequisites
*   Python 3.10+
*   Google Cloud API Key (for Gemini)

### 1. Clone the Repository
```bash
git clone https://github.com/Fainaz96/Project-Applicant-Tracking-System-ATS.git
cd Project-Applicant-Tracking-System-ATS
```

### 2. Create Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory:
```ini
SECRET_KEY=your_django_secret_key
DEBUG=True
GOOGLE_API_KEY=your_google_gemini_api_key
```

### 5. Apply Migrations
```bash
python manage.py migrate
```

### 6. Create Admin User (Optional)
```bash
python manage.py createsuperuser
```

### 7. Run the Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to see the application.

---

## 📖 Usage Guide

### For Candidates
1.  Navigate to the **Home Page**.
2.  Select an open position (e.g., "AI Engineer").
3.  Click **Apply Now**.
4.  Upload your resume (PDF/DOCX).
5.  Receive confirmation of application.

### For Recruiters
1.  Go to `http://127.0.0.1:8000/dashboard/`.
2.  View the list of all applicants.
3.  See the **AI Score** (Total, Skills, Experience) for each candidate.
4.  Click on a candidate's name to view the detailed evaluation and AI reasoning.

---

## 📂 Project Structure

```
.
├── ats/                    # Main Application App
│   ├── agents.py           # AI Agents (Parser, Ranker, Extractor)
│   ├── models.py           # Database Models (Job, Applicant, Skill)
│   ├── views.py            # Business Logic & Views
│   ├── vector_db.py        # ChromaDB Integration
│   └── templates/ats/      # HTML Templates
├── config/                 # Django Project Configuration
├── media/resumes/          # Uploaded Resume Files
├── chroma_db/              # Vector Database Storage
├── manage.py               # Django Management Script
├── requirements.txt        # Python Dependencies
└── README.md               # Project Documentation
```

---

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a Pull Request.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
