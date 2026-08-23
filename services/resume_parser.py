import fitz
import re
from typing import Dict, Any, List

class ResumeParser:
    EXTENDED_SKILL_CATALOG = [
        # Programming & Core
        "Python", "SQL", "C++", "Java", "TypeScript", "JavaScript", "Go", "Rust", "Bash", "R",
        # AI & LLM Frameworks
        "LLMs", "RAG", "AI Agents", "LangChain", "LangGraph", "LlamaIndex", "Transformers", 
        "Hugging Face", "DSPy", "Fine-Tuning / LoRA", "Prompt Engineering", "Vector Databases",
        "ChromaDB", "Pinecone", "Qdrant", "FAISS", "Weaviate", "Semantic Kernel",
        # ML & Deep Learning
        "Machine Learning", "Deep Learning", "PyTorch", "TensorFlow", "Keras", "Scikit-Learn",
        "OpenCV", "Object Detection", "NLP", "Computer Vision", "Reinforcement Learning",
        "Pandas", "NumPy", "SciPy", "Matplotlib", "Seaborn", "Plotly",
        # Data & Cloud Infrastructure
        "Spark", "Data Pipelines", "Kafka", "Airflow", "PostgreSQL", "MySQL", "MongoDB",
        "Redis", "Snowflake", "BigQuery", "Databricks", "dbt", "Cloud Data Warehouse",
        # DevOps, MLOps & Architecture
        "Docker", "Kubernetes", "MLOps", "MLflow", "Kubeflow", "Weights & Biases", "CI/CD",
        "AWS", "GCP", "Azure", "Linux", "Git", "System Design", "Distributed Systems",
        "FastAPI", "Flask", "Django", "React / Next.js", "GraphQL", "REST APIs",
        "Data Structures & Algorithms", "A/B Testing", "Statistics & Probability"
    ]

    @staticmethod
    def extract_text_from_pdf(pdf_bytes: bytes) -> str:
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")
        return "\n".join([page.get_text() for page in doc])

    @staticmethod
    def parse_profile(raw_text: str) -> Dict[str, Any]:
        detected_skills: Dict[str, int] = {}
        
        # Detect skills from catalog with regex boundaries
        for skill in ResumeParser.EXTENDED_SKILL_CATALOG:
            # Handle special characters like C++, /
            escaped = re.escape(skill)
            if re.search(rf"(?:^|\W){escaped}(?:$|\W)", raw_text, re.IGNORECASE):
                # Count frequency or mention context to estimate proficiency (6-9)
                mentions = len(re.findall(rf"(?:^|\W){escaped}(?:$|\W)", raw_text, re.IGNORECASE))
                rating = min(9, 6 + (1 if mentions > 1 else 0) + (1 if mentions > 3 else 0))
                detected_skills[skill] = rating

        # Candidate Name extraction heuristic
        lines = [line.strip() for line in raw_text.splitlines() if line.strip()]
        candidate_name = "Candidate"
        for line in lines[:5]:
            # Look for lines without numbers or email symbols that look like names
            if re.match(r"^[A-Za-z\s\.\-']{3,35}$", line) and not any(kw in line.lower() for kw in ["resume", "curriculum", "page", "email", "phone"]):
                candidate_name = line.strip()
                break

        # Experience years heuristic
        exp_match = re.search(r"(\d+(\.\d+)?)\+?\s*(?:years?|yrs?)(?:\s+of)?\s+(?:experience|work)", raw_text, re.IGNORECASE)
        if exp_match:
            exp_years = float(exp_match.group(1))
        else:
            # Date range detection like 2020 - 2024
            years = re.findall(r"\b(201\d|202\d)\b", raw_text)
            if len(years) >= 2:
                int_years = sorted([int(y) for y in years])
                exp_years = float(min(15, max(1, int_years[-1] - int_years[0])))
            else:
                exp_years = 2.5

        # Education heuristic
        education = "B.S. in Computer Science"
        if re.search(r"\b(Ph\.?D|Doctorate)\b", raw_text, re.IGNORECASE):
            education = "Ph.D. in Computer Science / AI"
        elif re.search(r"\b(M\.?S\.?|Master(?:'s)?)\b", raw_text, re.IGNORECASE):
            education = "M.S. in Computer Science / AI"
        elif re.search(r"\b(B\.?S\.?|Bachelor(?:'s)?|B\.Tech|B\.E\.)\b", raw_text, re.IGNORECASE):
            education = "B.S. in Computer Science / Engineering"

        if not detected_skills:
            detected_skills = {"Python": 7, "SQL": 6, "Machine Learning": 6, "Docker": 5}

        return {
            "name": candidate_name[:40],
            "skills": detected_skills,
            "education": education,
            "experience_years": exp_years,
            "raw_text": raw_text
        }
