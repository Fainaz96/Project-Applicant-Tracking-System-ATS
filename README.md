# 🚀 AI-Powered Applicant Tracking System (ATS)

An intelligent recruitment platform that leverages Google's Gemini AI to automate resume screening, parsing, skill extraction, and candidate ranking. This system helps recruiters save time by instantly identifying the best candidates for specific job roles.

---

## 🌟 Key Features

*   **🤖 AI Resume Parsing**: Automatically extracts candidate details (Name, Email, Phone, Experience) from PDF and DOCX resumes using Gemini 1.5 Flash.
*   **🎯 Context-Aware Ranking**: ranks candidates specifically against the **Job Description** they applied for, providing a relevance score (0-100%).
*   **💼 Job Board & Career Page**: A public-facing career page where candidates can browse open positions and apply directly.
*   **🧠 Skill Extraction**: Identifies technical and soft skills and saves them to the database.
*   **⚡ Lightweight Vector Search**: Uses **Gemini Embeddings** + JSON storage for semantic search, optimized for serverless deployment (removing heavy request for ChromaDB).
*   **📊 Recruiter Dashboard**: A centralized view to manage applicants, view AI evaluations, and sort candidates by best fit.

---

## 🛠️ Tech Stack

*   **Backend**: Django 5.0 (Python)
*   **AI Model**: Google Gemini 2.5 Flash / Flash Lite (via `google-generativeai`)
*   **Vector Database**: Custom Lightweight JSON Store (optimized for Vercel)
*   **Database**: SQLite (Development/Demo)
*   **Frontend**: HTML5, CSS3, Django Templates
*   **Deployment**: Vercel (Serverless)

---

## 🚀 Live Demo (Vercel)

This project is deployed on Vercel!
**Note**: Since Vercel is serverless and read-only:
1.  **Database Reset**: The SQLite database resets to its initial state every time the app redeploys or sleeps. New data persists only for the active session.
2.  **File Uploads**: Resumes are processed in `/tmp` (ephemeral storage) and are not permanently stored on the server.

---

## ⚙️ Installation & Setup

### Prerequisites
*   Python 3.10+
*   Google Cloud API Key (for Gemini)

### 1. Clone the Repository
```bash
git clone https://github.com/StartAgain00/Project-Applicant-Tracking-System-ATS.git
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

## ☁️ Deployment Guide (Vercel)

This project is configured for easy deployment on **Vercel**.

1.  **Fork** this repository.
2.  Login to [Vercel](https://vercel.com/) and click **"Add New Project"**.
3.  Import your forked repository.
4.  **Environment Variables**: Add the keys from your `.env` file (`GOOGLE_API_KEY`, `SECRET_KEY`, `DEBUG=False`) to the Vercel project settings.
5.  **Deploy**!

Vercel Configuration files `vercel.json` and `wsgi.py` are pre-configured.

---

## 📂 Project Structure

```
.
├── ats/                    # Main Application App
│   ├── agents.py           # AI Agents (Parser, Ranker, Extractor)
│   ├── models.py           # Database Models
│   ├── views.py            # Business Logic
│   ├── vector_db.py        # Lightweight Vector DB (JSON + Gemini)
│   └── templates/ats/      # HTML Templates
├── config/                 # Django Project Config
├── media/                  # Resume Storage
├── vercel.json             # Vercel Deployment Config
├── manage.py               # Django Management Script
├── requirements.txt        # Python Dependencies
└── README.md               # Documentation
```

---

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a Pull Request.

---

## 📄 License

This project is open-source.
