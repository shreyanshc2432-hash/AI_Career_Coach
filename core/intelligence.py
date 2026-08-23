import re
from typing import Dict, List, Tuple, Any

ROLE_BENCHMARKS: Dict[str, Dict[str, Tuple[int, int]]] = {
    "Generative AI Engineer": {
        "Python": (9, 5),
        "LLMs": (9, 5),
        "RAG": (9, 5),
        "AI Agents": (8, 5),
        "LangChain": (8, 4),
        "Vector Databases": (8, 4),
        "FastAPI": (7, 4),
        "Docker": (7, 3),
        "System Design": (8, 4),
        "Machine Learning": (7, 3),
        "Deep Learning": (7, 3)
    },
    "Machine Learning Engineer": {
        "Python": (9, 5),
        "Machine Learning": (9, 5),
        "Deep Learning": (8, 5),
        "PyTorch": (8, 5),
        "SQL": (8, 4),
        "MLOps": (7, 4),
        "Docker": (7, 3),
        "System Design": (7, 4),
        "Data Structures & Algorithms": (8, 4),
        "Pandas": (8, 3)
    },
    "Data Scientist": {
        "Python": (9, 5),
        "SQL": (9, 5),
        "Machine Learning": (8, 5),
        "Statistics & Probability": (9, 5),
        "Pandas": (9, 4),
        "Data Visualization": (8, 4),
        "A/B Testing": (8, 4),
        "Deep Learning": (6, 3),
        "Docker": (5, 2)
    },
    "Data Engineer": {
        "SQL": (9, 5),
        "Python": (9, 5),
        "Spark": (8, 5),
        "Data Pipelines": (9, 5),
        "PostgreSQL": (8, 4),
        "Kafka": (7, 4),
        "Airflow": (8, 4),
        "Cloud Data Warehouse": (8, 4),
        "Docker": (7, 3),
        "System Design": (8, 4)
    },
    "MLOps Engineer": {
        "Python": (8, 4),
        "Docker": (9, 5),
        "Kubernetes": (9, 5),
        "CI/CD": (9, 5),
        "MLOps": (9, 5),
        "Model Monitoring": (8, 4),
        "Cloud (AWS/GCP)": (8, 4),
        "System Design": (8, 4),
        "Git": (8, 3)
    },
    "AI Solutions Architect": {
        "System Design": (9, 5),
        "Cloud Architecture": (9, 5),
        "LLMs": (8, 5),
        "Distributed Systems": (8, 4),
        "Enterprise Security": (8, 4),
        "Python": (7, 3),
        "AI Strategy": (9, 5),
        "Docker": (7, 3)
    },
    "Computer Vision Engineer": {
        "Python": (9, 5),
        "PyTorch": (9, 5),
        "OpenCV": (9, 5),
        "Deep Learning": (9, 5),
        "Object Detection": (8, 4),
        "Edge AI / TensorRT": (7, 4),
        "C++": (7, 3),
        "Linear Algebra": (8, 4)
    },
    "NLP & LLM Engineer": {
        "Python": (9, 5),
        "Transformers": (9, 5),
        "LLMs": (9, 5),
        "PyTorch": (8, 4),
        "Fine-Tuning / LoRA": (8, 5),
        "RAG": (8, 4),
        "Prompt Engineering": (8, 4),
        "Vector Databases": (7, 3)
    },
    "Full-Stack AI Engineer": {
        "Python": (8, 5),
        "FastAPI": (8, 4),
        "React / Next.js": (8, 4),
        "TypeScript": (7, 4),
        "SQL": (7, 3),
        "LLM Integration": (8, 5),
        "Docker": (7, 3),
        "Vector Databases": (7, 3)
    },
    "AI Product & Analytics Specialist": {
        "AI/ML Fundamentals": (8, 5),
        "Product Roadmap": (9, 5),
        "SQL": (8, 4),
        "Metrics & KPIs": (9, 5),
        "Prompt Prototyping": (7, 4),
        "A/B Testing": (8, 4),
        "User Research": (8, 4)
    }
}

class CareerIntelligenceEngine:
    @staticmethod
    def calculate_skill_gaps(current_skills: Dict[str, int], required_skills: Dict[str, Tuple[int, int]]) -> List[Dict]:
        gap_analysis = []
        for skill, (target_lvl, importance) in required_skills.items():
            curr_lvl = current_skills.get(skill, 0)
            gap = max(0, target_lvl - curr_lvl)
            priority_score = importance * gap
            gap_analysis.append({
                "skill": skill,
                "current_level": curr_lvl,
                "target_level": target_lvl,
                "gap": gap,
                "importance": importance,
                "priority_score": priority_score,
                "status": "Ready" if gap == 0 else ("Minor Gap" if gap <= 2 else "Critical Gap")
            })
        return sorted(gap_analysis, key=lambda x: x["priority_score"], reverse=True)

    @staticmethod
    def calculate_readiness_score(current_skills: Dict[str, int], required_skills: Dict[str, Tuple[int, int]]) -> float:
        if not required_skills:
            return 0.0
        total_weight = 0
        achieved_weight = 0.0
        for skill, (target_lvl, importance) in required_skills.items():
            curr_lvl = current_skills.get(skill, 0)
            effective_ratio = min(1.0, curr_lvl / target_lvl if target_lvl > 0 else 1.0)
            total_weight += (target_lvl * importance)
            achieved_weight += (curr_lvl * importance * effective_ratio)
        if total_weight == 0:
            return 100.0
        return min(100.0, max(0.0, round((achieved_weight / total_weight) * 100, 1)))

    @staticmethod
    def calculate_job_match(candidate_skills: List[str], required_skills: List[str], preferred_skills: List[str]) -> Dict:
        cand_set = {s.lower().strip() for s in candidate_skills}
        req_set = {s.lower().strip() for s in required_skills}
        pref_set = {s.lower().strip() for s in preferred_skills}
        matched_req = cand_set.intersection(req_set)
        missing_req = req_set - cand_set
        matched_pref = cand_set.intersection(pref_set)
        missing_pref = pref_set - cand_set
        req_score = (len(matched_req) / len(req_set)) if req_set else 1.0
        pref_score = (len(matched_pref) / len(pref_set)) if pref_set else 1.0
        total_match = round((req_score * 0.75 + pref_score * 0.25) * 100, 1)
        return {
            "match_percentage": total_match,
            "matched_required": [s.title() for s in matched_req],
            "missing_required": [s.title() for s in missing_req],
            "matched_preferred": [s.title() for s in matched_pref],
            "missing_preferred": [s.title() for s in missing_pref]
        }

    @staticmethod
    def evaluate_multi_role_strength(candidate_skills: Dict[str, int]) -> List[Dict[str, Any]]:
        results = []
        cand_skill_lower = {k.lower().strip(): v for k, v in candidate_skills.items()}

        for role_name, benchmarks in ROLE_BENCHMARKS.items():
            readiness = CareerIntelligenceEngine.calculate_readiness_score(candidate_skills, benchmarks)
            
            matched_skills = []
            missing_skills = []
            
            for skill, (req_lvl, imp) in benchmarks.items():
                curr = candidate_skills.get(skill, 0)
                if curr == 0:
                    # check case-insensitive match
                    curr = cand_skill_lower.get(skill.lower().strip(), 0)
                
                if curr >= (req_lvl - 2) and curr > 0:
                    matched_skills.append(skill)
                else:
                    missing_skills.append(skill)

            coverage_ratio = len(matched_skills) / len(benchmarks) if benchmarks else 0.0
            match_percentage = round((readiness * 0.6 + coverage_ratio * 100 * 0.4), 1)

            if match_percentage >= 75:
                fit_level = "🟢 High Fit"
            elif match_percentage >= 50:
                fit_level = "🟡 Moderate Fit"
            else:
                fit_level = "🔴 Needs Upskilling"

            results.append({
                "role_name": role_name,
                "match_percentage": match_percentage,
                "readiness_score": readiness,
                "fit_level": fit_level,
                "matched_skills": matched_skills,
                "missing_skills": missing_skills,
                "total_benchmark_skills": len(benchmarks)
            })

        return sorted(results, key=lambda x: x["match_percentage"], reverse=True)

    @staticmethod
    def audit_resume_quality(raw_text: str, candidate_skills: Dict[str, int]) -> Dict[str, Any]:
        # Power action verbs
        power_verbs = [
            "architected", "engineered", "developed", "deployed", "spearheaded",
            "optimized", "scaled", "automated", "orchestrated", "reduced",
            "accelerated", "implemented", "fine-tuned", "designed", "streamlined",
            "trained", "integrated", "boosted", "delivered", "built", "managed"
        ]
        
        lower_text = raw_text.lower()
        verbs_found = [v.title() for v in power_verbs if re.search(rf"\b{v}\b", lower_text)]
        
        # Metric and quantification detection (e.g. 45%, $1.2M, 10x, 200ms, 5k users)
        metric_patterns = [
            r"\b\d+%\b",
            r"\$\d+[\d,]*(\.\d+)?[kKmMbB]?",
            r"\b\d+x\b",
            r"\b\d+\s*(ms|seconds|minutes|hours|days|requests|users|qps|gb|tb|pb)\b",
            r"\breduced\s+by\s+\d+",
            r"\bincreased\s+by\s+\d+",
            r"\bimproved\s+by\s+\d+"
        ]
        total_metrics = 0
        for pat in metric_patterns:
            matches = re.findall(pat, raw_text, re.IGNORECASE)
            total_metrics += len(matches)

        # Basic ATS section checks
        has_experience = bool(re.search(r"\b(experience|work history|employment)\b", lower_text))
        has_education = bool(re.search(r"\b(education|university|degree|bachelor|master|phd|b\.s|m\.s)\b", lower_text))
        has_projects = bool(re.search(r"\b(projects|portfolio|open source|publications)\b", lower_text))
        has_skills_section = bool(re.search(r"\b(skills|technical proficiencies|technologies)\b", lower_text))

        # Scoring heuristics
        ats_base = 50
        if has_experience: ats_base += 12
        if has_education: ats_base += 12
        if has_skills_section: ats_base += 13
        if has_projects: ats_base += 13
        ats_score = min(100, max(30, ats_base))

        # Impact score based on metrics count
        impact_score = min(100, max(25, 40 + total_metrics * 10))

        # Action verb score
        action_verb_score = min(100, max(30, len(verbs_found) * 12))

        # Tips
        tips = []
        if total_metrics < 3:
            tips.append("💡 Add more quantified metrics (e.g., 'Reduced latency by 45%', 'Scaled pipeline to 2M QPS').")
        else:
            tips.append("✅ Great use of quantifiable business impact and performance metrics.")

        if len(verbs_found) < 4:
            tips.append("💡 Start bullet points with strong action verbs (e.g. 'Architected', 'Spearheaded', 'Optimized').")
        else:
            tips.append(f"✅ Strong action verbs detected ({', '.join(verbs_found[:4])}).")

        if len(candidate_skills) < 6:
            tips.append("💡 Add more domain-specific tools and frameworks to improve ATS keyword discoverability.")

        return {
            "ats_score": ats_score,
            "impact_score": impact_score,
            "action_verb_score": action_verb_score,
            "verbs_found": verbs_found,
            "total_metrics": total_metrics,
            "tips": tips
        }
