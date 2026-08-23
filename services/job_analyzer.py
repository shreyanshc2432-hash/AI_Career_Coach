import re
from typing import Dict, List

class JobDescriptionAnalyzer:
    @staticmethod
    def extract_requirements(jd_text: str) -> Dict[str, List[str]]:
        skill_catalog = [
            "Python", "SQL", "C++", "Java", "PyTorch", "TensorFlow",
            "FastAPI", "Docker", "Kubernetes", "AWS", "GCP", "Azure",
            "RAG", "LLMs", "LangChain", "AI Agents", "System Design",
            "DSA", "Distributed Systems", "PostgreSQL", "Machine Learning"
        ]
        found = [s for s in skill_catalog if re.search(rf"\b{re.escape(s)}\b", jd_text, re.IGNORECASE)]
        if len(found) > 4:
            return {"required_skills": found[:4], "preferred_skills": found[4:]}
        return {"required_skills": found if found else ["Python", "SQL"], "preferred_skills": ["Docker", "Cloud"]}
