from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any

class CandidateProfile(BaseModel):
    name: str = "Candidate"
    target_role: str = "Generative AI Engineer"
    experience_years: float = 1.0
    education: str = "B.S. in Computer Science"
    skills: Dict[str, int] = Field(default_factory=dict)
    target_salary: str = "$120,000"
    preferred_location: str = "Remote / Hybrid"

class ProjectBlueprint(BaseModel):
    title: str
    role_category: str = "Generative AI"
    difficulty: str = "Advanced / Enterprise"
    domain: str = "Fintech & Enterprise"
    estimated_hours: str = "40-60 Hours"
    summary: str
    tech_stack: List[str]
    skills_developed: List[str]
    architecture_overview: str
    milestones: List[str]
    resume_bullet_points: List[str]
    sample_interview_questions: List[str]
    github_readme_preview: Optional[str] = None
    production_gotchas: Optional[List[str]] = None

class RoleMatchSummary(BaseModel):
    role_name: str
    match_percentage: float
    fit_level: str
    matched_skills: List[str]
    missing_skills: List[str]
    readiness_score: float

class ResumeAuditResult(BaseModel):
    ats_score: int
    impact_score: int
    action_verb_score: int
    detected_name: str
    detected_experience_years: float
    skills: Dict[str, int]
    role_matches: List[RoleMatchSummary]
    top_recommended_role: str
    power_verbs_found: List[str]
    metrics_detected_count: int
    improvement_tips: List[str]
