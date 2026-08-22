import os
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Text
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

DATA_DIR = os.getenv("DATA_DIR", ".")
os.makedirs(DATA_DIR, exist_ok=True)
DATABASE_URL = f"sqlite:///{os.path.join(DATA_DIR, 'career_coach.db')}"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class JobApplication(Base):
    __tablename__ = "job_applications"
    id = Column(Integer, primary_key=True, index=True)
    company = Column(String(100), nullable=False)
    role = Column(String(100), nullable=False)
    status = Column(String(50), default="Applied")
    match_score = Column(Float, default=0.0)
    salary_range = Column(String(50), nullable=True)
    applied_date = Column(DateTime, default=datetime.utcnow)
    notes = Column(Text, nullable=True)

class InterviewSession(Base):
    __tablename__ = "interview_sessions"
    id = Column(Integer, primary_key=True, index=True)
    role = Column(String(100), nullable=False)
    question = Column(Text, nullable=False)
    user_answer = Column(Text, nullable=False)
    overall_score = Column(Float, default=0.0)
    technical_score = Column(Float, default=0.0)
    communication_score = Column(Float, default=0.0)
    problem_solving_score = Column(Float, default=0.0)
    behavioral_score = Column(Float, default=0.0)
    created_at = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()
