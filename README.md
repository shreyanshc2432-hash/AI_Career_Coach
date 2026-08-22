# 🚀 AI Career Coach

> **An AI-powered career guidance platform that analyzes your resume, identifies skill gaps, evaluates career readiness, and generates a personalized roadmap for your target career.**

---

## 📌 Overview

**AI Career Coach** is an AI-powered career guidance application designed to help students and job seekers understand where they currently stand in their career journey and what they should do next.

The application takes a user's **resume and target career role** as input and uses AI to generate:

* 📄 Resume analysis
* 🎯 Career readiness score
* 💪 Strength analysis
* 🧩 Skill-gap identification
* 🗺️ Personalized learning roadmap
* 💡 Project recommendations
* 🤖 AI-powered career guidance

The initial version is designed as a **6-hour MVP/demo project**, with a roadmap for expanding it into a complete AI career platform.

---

## 🎯 Problem Statement

Students and fresh graduates often struggle with questions such as:

* Which career should I choose?
* Am I ready for my target role?
* Which skills am I missing?
* What should I learn first?
* Which projects should I build?
* How can I improve my resume?
* What should I prepare for interviews?

Existing career platforms often provide generic recommendations.

**AI Career Coach aims to provide personalized recommendations based on the user's actual skills, experience, resume, and career goals.**

---

## 💡 Solution

The application follows this workflow:

```text
Resume + Target Career
        ↓
   Resume Analysis
        ↓
 Candidate Profile
        ↓
 Career Assessment
        ↓
 Skill Gap Analysis
        ↓
 Personalized Roadmap
        ↓
 Project Recommendations
        ↓
    AI Career Coach
```

---

## ✨ Key Features

### 📄 Resume Analyzer

Upload a PDF resume and extract important information such as:

* Education
* Technical skills
* Projects
* Experience
* Certifications
* Achievements

---

### 🎯 Career Assessment

Select a target career such as:

* Generative AI Developer
* Data Analyst
* Data Scientist
* Machine Learning Engineer
* Software Engineer

The system compares the candidate's current profile with the requirements of the selected career.

---

### 📊 Career Readiness Score

The AI generates an overall career-readiness score.

Example:

```text
Career Readiness: 74/100

Technical Skills     82%
Projects             71%
Experience           55%
Role Alignment       79%
```

---

### 🧩 Skill Gap Analysis

The application identifies both strengths and missing skills.

Example:

```text
✅ Python
✅ SQL
✅ Pandas
✅ Machine Learning

⚠️ RAG
⚠️ Vector Databases
⚠️ AI Agents
⚠️ Docker
```

---

### 🗺️ Personalized Learning Roadmap

Instead of giving every user the same learning plan, the AI generates a roadmap based on their individual skill gaps.

Example:

```text
Week 1 → LLM Fundamentals
Week 2 → RAG
Week 3 → Vector Databases
Week 4 → AI Agents
Week 5 → Deployment
```

---

### 💡 Project Recommendations

The system recommends projects that help users develop their missing skills.

Example:

**AI PDF Research Assistant**

Skills:

```text
Python
RAG
LLMs
Vector Databases
```

---

### 🤖 AI Career Coach

Users can interact with the AI and ask questions such as:

> "What should I learn next?"

> "Why is my career score low?"

> "Which projects should I build?"

> "How can I become a Generative AI Developer?"

---

# 🏗️ System Architecture

```text
                    ┌─────────────────┐
                    │      USER       │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │  Resume Upload  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │  PDF Extraction │
                    │    PyMuPDF      │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   AI Analysis   │
                    │    LLM API      │
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
       ┌────────────┐ ┌────────────┐ ┌────────────┐
       │ Career     │ │ Skill Gap  │ │ Strengths  │
       │   Score    │ │  Analysis  │ │  Analysis  │
       └─────┬──────┘ └─────┬──────┘ └─────┬──────┘
             │              │              │
             └──────────────┼──────────────┘
                            ▼
                  ┌───────────────────┐
                  │ Personalized      │
                  │ Career Roadmap    │
                  └─────────┬─────────┘
                            │
                            ▼
                  ┌───────────────────┐
                  │ Project           │
                  │ Recommendations   │
                  └─────────┬─────────┘
                            │
                            ▼
                  ┌───────────────────┐
                  │   AI Career Chat  │
                  └───────────────────┘
```

---

# 🛠️ Tech Stack

## Programming Language

**Python**

Python is used for the application logic, AI integration, data processing, and backend functionality.

## Frontend / UI

**Streamlit**

Used to create the interactive web interface without requiring a separate JavaScript frontend.

## AI

**LLM API**

Used for:

* Resume understanding
* Career analysis
* Skill-gap reasoning
* Roadmap generation
* Project recommendations
* Career conversations

## PDF Processing

**PyMuPDF**

Used to extract text from uploaded PDF resumes.

## Data Processing

**Pandas**

Used for data manipulation and analysis.

## Data Validation

**Pydantic**

Used to structure and validate AI-generated data.

## Configuration

**python-dotenv**

Used to securely load environment variables such as API keys.

---

# 📦 Project Structure

```text
AI-Career-Coach/
│
├── app.py                  # Main Streamlit application
│
├── resume_parser.py        # Resume PDF processing
│
├── career_engine.py        # Career scoring and skill-gap logic
│
├── ai_service.py           # LLM/API integration
│
├── prompts.py              # AI prompts
│
├── data/
│   └── career_roles.json   # Career role and skill requirements
│
├── .env                    # Environment variables
├── .gitignore
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/AI-Career-Coach.git
```

```bash
cd AI-Career-Coach
```

---

## 2. Create a virtual environment

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure API key

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

> **Never upload your `.env` file or API key to GitHub.**

Add `.env` to `.gitignore`.

---

# ▶️ Running the Application

Run:

```bash
streamlit run app.py
```

The application will open in your browser.

---

# 🧪 Example Workflow

### Step 1

Upload:

```text
resume.pdf
```

### Step 2

Select:

```text
Generative AI Developer
```

### Step 3

The system analyzes the resume.

### Step 4

It generates:

```text
Career Score: 74/100
```

### Step 5

It identifies:

```text
Strengths:
Python
SQL
Machine Learning

Skill Gaps:
RAG
Vector Databases
AI Agents
Docker
```

### Step 6

It generates a personalized learning roadmap.

### Step 7

It recommends projects to close the identified skill gaps.

---

# 🚀 Future Development

The current project is an MVP. Future versions can include:

* 🔍 Real-time job matching
* 💼 Job application tracking
* 🎤 AI mock interviews
* 🗣️ Voice-based interviews
* 📊 Career progress analytics
* 📚 RAG-based career knowledge base
* 🤖 Agentic AI career assistant
* 📄 ATS resume optimization
* 🏢 Company-specific preparation
* 🎯 Personalized interview preparation
* 🔔 Career progress notifications
* ☁️ Cloud deployment
* 💳 Premium subscription system

---

# 🧠 Future Agentic Architecture

The long-term version can contain specialized AI agents:

```text
                    CAREER AGENT
                         │
       ┌─────────────────┼─────────────────┐
       ▼                 ▼                 ▼
 Resume Agent        Job Agent       Learning Agent
       │                 │                 │
       ▼                 ▼                 ▼
Interview Agent     Project Agent     Skill Agent
       │                 │                 │
       └─────────────────┼─────────────────┘
                         ▼
                  Career Dashboard
```

The ultimate goal is to create an AI system that continuously understands a user's career goals, identifies skill gaps, recommends what to learn and build next, and helps them prepare for their target jobs.

---

# 💰 Potential Business Model

The application can follow a **Freemium SaaS model**.

### Free

* Basic resume analysis
* Limited career assessments
* Basic skill-gap analysis

### Pro

* Unlimited resume analysis
* Personalized roadmaps
* Project generation
* Advanced career analysis
* Mock interviews

### Premium

* AI voice interviews
* Job matching
* Application tracking
* Advanced career agent
* Company-specific preparation

---

# 🎓 Academic Value

This project demonstrates practical implementation of:

* Artificial Intelligence
* Generative AI
* Natural Language Processing
* PDF document processing
* Prompt engineering
* Data processing
* Recommendation systems
* Web application development
* API integration
* Career analytics

It can therefore serve as both an **academic project/demo** and a foundation for a potential real-world SaaS product.

---

# 👥 Team

### Team Name

**Error 404**

### Team Members

* Shreyansh
* Prince
* Ayush
* Nikhil

---

# 📌 Current Status

```text
🚧 MVP / Demo Version
```

The current version focuses on the core functionality:

```text
Resume
  ↓
AI Analysis
  ↓
Career Score
  ↓
Skill Gap
  ↓
Personalized Roadmap
  ↓
Project Recommendations
```

---

# ⭐ Why This Project?

Traditional career guidance provides generic advice.

**AI Career Coach aims to make career guidance personalized, adaptive, and AI-driven.**

> **Your resume tells us where you are.
> Your goal tells us where you want to go.
> AI Career Coach tells you how to get there.**

---

## 📄 License

This project is intended primarily for educational, demonstration, and experimental purposes.

Add an appropriate open-source license before public commercial distribution.
