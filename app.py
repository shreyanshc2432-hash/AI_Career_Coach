import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

from core.intelligence import CareerIntelligenceEngine, ROLE_BENCHMARKS
from services.resume_parser import ResumeParser
from services.job_analyzer import JobDescriptionAnalyzer
from services.roadmap_service import RoadmapService
from services.project_generator import ProjectGeneratorService
from services.interview_service import MockInterviewService
from database import get_db, JobApplication, InterviewSession

st.set_page_config(
    page_title="AI Career Coach & Portfolio Intelligence",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize Session State Profile
if "profile" not in st.session_state:
    st.session_state.profile = {
        "name": "Alex Mercer",
        "target_role": "Generative AI Engineer",
        "experience_years": 2.5,
        "education": "B.S. in Computer Science",
        "skills": {
            "Python": 8,
            "SQL": 7,
            "Machine Learning": 7,
            "Deep Learning": 5,
            "LLMs": 6,
            "RAG": 4,
            "AI Agents": 3,
            "LangChain": 5,
            "Docker": 6,
            "FastAPI": 6,
            "System Design": 5,
            "Vector Databases": 4,
            "Git": 8
        },
        "raw_resume_text": ""
    }

# ----------------- SIDEBAR -----------------
st.sidebar.title("🎯 AI Career Coach")
st.sidebar.caption("Accelerate your career with AI-driven skill intelligence.")

# Role Switcher in Sidebar
available_roles = list(ROLE_BENCHMARKS.keys())
current_role = st.session_state.profile.get("target_role", "Generative AI Engineer")
if current_role not in available_roles:
    current_role = available_roles[0]

selected_role = st.sidebar.selectbox(
    "🎯 Target Job Role",
    options=available_roles,
    index=available_roles.index(current_role),
    help="Switch roles to instantly recalculate readiness scores, skill gaps, roadmaps, project blueprints, and interview simulations."
)
if selected_role != st.session_state.profile["target_role"]:
    st.session_state.profile["target_role"] = selected_role
    st.rerun()

st.sidebar.markdown(f"**Candidate:** `{st.session_state.profile['name']}`")
st.sidebar.markdown(f"**Exp:** `{st.session_state.profile.get('experience_years', 2.0)} yrs` | **Edu:** `{st.session_state.profile.get('education', 'CS Background')}`")

st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    [
        "📊 Executive Dashboard",
        "📄 Resume Analyzer & Multi-Role Audit",
        "⚖️ Skill Gap & Benchmarks",
        "🔍 Job Match Engine",
        "🗺️ Personalized Roadmap",
        "💡 AI Portfolio Project Generator",
        "🎙️ Mock Interview Simulator",
        "📋 Job Application Tracker"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("💡 **Tip:** Switch job roles above or in the Resume Analyzer to test your market readiness across different specialties.")

# Active Role Benchmarks & Calculations
active_role = st.session_state.profile["target_role"]
req_benchmarks = ROLE_BENCHMARKS.get(active_role, ROLE_BENCHMARKS["Generative AI Engineer"])
readiness = CareerIntelligenceEngine.calculate_readiness_score(st.session_state.profile["skills"], req_benchmarks)
skill_gaps = CareerIntelligenceEngine.calculate_skill_gaps(st.session_state.profile["skills"], req_benchmarks)
multi_role_strengths = CareerIntelligenceEngine.evaluate_multi_role_strength(st.session_state.profile["skills"])


# ==========================================
# PAGE 1: EXECUTIVE DASHBOARD
# ==========================================
if page == "📊 Executive Dashboard":
    st.title("🚀 Career Readiness Executive Dashboard")
    st.markdown(f"Active Target: **{active_role}** | Candidate: **{st.session_state.profile['name']}**")

    db = get_db()
    total_apps = db.query(JobApplication).count()
    interviews = db.query(JobApplication).filter(JobApplication.status == "Interview").count()
    interview_count = db.query(InterviewSession).count()

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("🎯 Target Role", active_role)
    col2.metric("📈 Readiness Score", f"{readiness}%", delta=f"{readiness - 50:.1f}% vs Baseline")
    col3.metric("📋 Applications Tracked", total_apps, delta=f"{interviews} in interview")
    col4.metric("🎙️ Mock Interviews Completed", interview_count)

    st.markdown("---")

    col_gauge, col_radar = st.columns([1, 1.2])

    with col_gauge:
        st.subheader("🎯 Market Readiness Score")
        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=readiness,
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': f"{active_role}", 'font': {'size': 16}},
            gauge={
                'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "#475569"},
                'bar': {'color': "#2563EB"},
                'bgcolor': "white",
                'borderwidth': 2,
                'bordercolor': "#E2E8F0",
                'steps': [
                    {'range': [0, 50], 'color': "#FEE2E2"},
                    {'range': [50, 75], 'color': "#FEF3C7"},
                    {'range': [75, 100], 'color': "#D1FAE5"}
                ],
                'threshold': {'line': {'color': "#10B981", 'width': 4}, 'thickness': 0.8, 'value': 80}
            }
        ))
        fig_gauge.update_layout(height=300, margin=dict(l=20, r=20, t=40, b=20))
        st.plotly_chart(fig_gauge, use_container_width=True)

    with col_radar:
        st.subheader("🕸️ Candidate vs Benchmark Radar")
        radar_categories = [g["skill"] for g in skill_gaps]
        curr_values = [g["current_level"] for g in skill_gaps]
        target_values = [g["target_level"] for g in skill_gaps]

        if radar_categories:
            # Close the radar loop
            radar_categories.append(radar_categories[0])
            curr_values.append(curr_values[0])
            target_values.append(target_values[0])

            fig_radar = go.Figure()
            fig_radar.add_trace(go.Scatterpolar(
                r=target_values,
                theta=radar_categories,
                fill='toself',
                name='Role Benchmark',
                line_color='#94A3B8',
                fillcolor='rgba(148, 163, 184, 0.2)'
            ))
            fig_radar.add_trace(go.Scatterpolar(
                r=curr_values,
                theta=radar_categories,
                fill='toself',
                name='Your Profile',
                line_color='#2563EB',
                fillcolor='rgba(37, 99, 235, 0.3)'
            ))
            fig_radar.update_layout(
                polar=dict(radialaxis=dict(visible=True, range=[0, 10])),
                showlegend=True,
                height=300,
                margin=dict(l=40, r=40, t=20, b=20)
            )
            st.plotly_chart(fig_radar, use_container_width=True)

    st.markdown("---")

    col_gap, col_cross = st.columns([1.3, 1])

    with col_gap:
        st.subheader("📊 Skill Proficiency vs Benchmark")
        df_skills = pd.DataFrame(skill_gaps)
        fig_bar = px.bar(
            df_skills,
            x="skill",
            y=["current_level", "target_level"],
            barmode="group",
            labels={"value": "Proficiency (0-10)", "skill": "Skill", "variable": "Benchmark"},
            color_discrete_map={"current_level": "#3B82F6", "target_level": "#94A3B8"}
        )
        fig_bar.update_layout(height=320, margin=dict(l=20, r=20, t=30, b=40), xaxis_tickangle=-30)
        st.plotly_chart(fig_bar, use_container_width=True)

    with col_cross:
        st.subheader("🌐 Cross-Role Match Overview")
        df_roles = pd.DataFrame(multi_role_strengths[:5])
        fig_roles = px.bar(
            df_roles,
            x="match_percentage",
            y="role_name",
            orientation="h",
            labels={"match_percentage": "Match %", "role_name": "Role"},
            color="match_percentage",
            color_continuous_scale=["#EF4444", "#F59E0B", "#10B981"]
        )
        fig_roles.update_layout(height=320, margin=dict(l=20, r=20, t=30, b=20), yaxis=dict(autorange="reversed"))
        st.plotly_chart(fig_roles, use_container_width=True)

    st.subheader("⚡ High Priority Focus Areas (Priority = Importance × Gap)")
    top_gaps = [g for g in skill_gaps if g["gap"] > 0][:3]
    if top_gaps:
        cols = st.columns(len(top_gaps))
        for idx, item in enumerate(top_gaps):
            with cols[idx]:
                st.warning(
                    f"**{item['skill']}** (Gap: **{item['gap']} pts**)\n\n"
                    f"Priority Score: **{item['priority_score']}** | Importance: **{item['importance']}/5**\n\n"
                    f"Current: `{item['current_level']}/10` ➡️ Target: `{item['target_level']}/10`"
                )
    else:
        st.success(f"🎉 Fantastic! Your skill ratings meet or exceed all benchmarks for **{active_role}**!")


# ==========================================
# PAGE 2: RESUME ANALYZER & MULTI-ROLE AUDIT
# ==========================================
elif page == "📄 Resume Analyzer & Multi-Role Audit":
    st.title("📄 Intelligent Resume Parser & Multi-Role Strength Engine")
    st.markdown("Upload your resume in PDF format to detect skills, audit ATS compliance, and benchmark your strength across **10+ modern tech roles**.")

    uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"], help="Supported format: PDF up to 10MB")
    
    if uploaded_file:
        with st.spinner("Extracting text and performing comprehensive AI analysis..."):
            pdf_bytes = uploaded_file.read()
            raw_text = ResumeParser.extract_text_from_pdf(pdf_bytes)
            extracted = ResumeParser.parse_profile(raw_text)
            st.session_state.profile["raw_resume_text"] = raw_text

            st.success(f"✅ Resume successfully parsed for **{extracted['name']}**!")

            col_res_l, col_res_r = st.columns([1, 1])
            with col_res_l:
                st.subheader("👤 Detected Profile Information")
                st.markdown(f"**Name:** `{extracted['name']}`")
                st.markdown(f"**Estimated Experience:** `{extracted['experience_years']} years`")
                st.markdown(f"**Education:** `{extracted['education']}`")
                st.markdown(f"**Detected Skills ({len(extracted['skills'])}):** {', '.join(extracted['skills'].keys())}")
            
            with col_res_r:
                st.subheader("🔄 Synchronize Active Profile")
                st.info("Sync detected skills and candidate details into your active working profile.")
                if st.button("🚀 Sync Extracted Skills into Active Profile", type="primary"):
                    st.session_state.profile["skills"].update(extracted["skills"])
                    st.session_state.profile["name"] = extracted["name"]
                    st.session_state.profile["experience_years"] = extracted["experience_years"]
                    st.session_state.profile["education"] = extracted["education"]
                    st.success("Profile updated successfully! Refreshing dashboard...")
                    st.rerun()

    st.markdown("---")

    # Multi-Role Strength Matrix Section
    st.header("🎯 Resume Strength Across Different Job Roles")
    st.markdown("See how your current resume and skills measure up across diverse technical career paths.")

    # Calculate multi-role strengths from active profile skills
    strengths = CareerIntelligenceEngine.evaluate_multi_role_strength(st.session_state.profile["skills"])
    df_strengths = pd.DataFrame(strengths)

    c_chart1, c_chart2 = st.columns([1.2, 1])
    with c_chart1:
        st.subheader("📊 Role Strength & Match Ranking")
        fig_strength_bar = px.bar(
            df_strengths,
            x="match_percentage",
            y="role_name",
            orientation="h",
            text="match_percentage",
            labels={"match_percentage": "Match Score (%)", "role_name": "Job Role"},
            color="match_percentage",
            color_continuous_scale=["#EF4444", "#F59E0B", "#10B981"]
        )
        fig_strength_bar.update_layout(height=420, yaxis=dict(autorange="reversed"))
        fig_strength_bar.update_traces(texttemplate='%{text}%', textposition='outside')
        st.plotly_chart(fig_strength_bar, use_container_width=True)

    with c_chart2:
        st.subheader("🏆 Top Recommended Role Fit")
        top_fit = strengths[0]
        st.success(
            f"### 🥇 Top Fit: **{top_fit['role_name']}**\n\n"
            f"**Match Score:** `{top_fit['match_percentage']}%` ({top_fit['fit_level']})\n\n"
            f"**Readiness Score:** `{top_fit['readiness_score']}%`\n\n"
            f"**Matched Skills ({len(top_fit['matched_skills'])}):** {', '.join(top_fit['matched_skills'])}\n\n"
            f"**Missing Critical Skills:** {', '.join(top_fit['missing_skills']) if top_fit['missing_skills'] else 'None'}"
        )
        if st.button(f"🎯 Switch Target Role to '{top_fit['role_name']}'", key="switch_top_role"):
            st.session_state.profile["target_role"] = top_fit["role_name"]
            st.rerun()

    st.subheader("📋 Comprehensive Multi-Role Compatibility Breakdown")
    for s in strengths:
        with st.expander(f"{s['fit_level']} | **{s['role_name']}** — **{s['match_percentage']}% Match** (Readiness: {s['readiness_score']}%)"):
            col_a, col_b, col_c = st.columns([2, 2, 1])
            with col_a:
                st.markdown(f"**✅ Matched Skills ({len(s['matched_skills'])}/{s['total_benchmark_skills']}):**")
                if s["matched_skills"]:
                    st.write(", ".join([f"`{sk}`" for sk in s["matched_skills"]]))
                else:
                    st.write("No matching skills detected.")
            with col_b:
                st.markdown(f"**⚠️ Missing / Low Proficiency Skills ({len(s['missing_skills'])}):**")
                if s["missing_skills"]:
                    st.write(", ".join([f"`{sk}`" for sk in s["missing_skills"]]))
                else:
                    st.write("All benchmark skills covered!")
            with col_c:
                st.write("")
                if st.button(f"Select Role", key=f"btn_role_{s['role_name']}"):
                    st.session_state.profile["target_role"] = s["role_name"]
                    st.rerun()

    # Resume Quality & ATS Heuristics Audit
    st.markdown("---")
    st.header("🔍 Resume Quality & ATS Heuristic Audit")
    
    sample_audit_text = st.session_state.profile.get("raw_resume_text", "")
    if not sample_audit_text:
        sample_audit_text = f"Candidate Profile: {st.session_state.profile['name']}. Experienced in {', '.join(st.session_state.profile['skills'].keys())}. Developed scalable architectures and reduced latency by 35%."
    
    audit_res = CareerIntelligenceEngine.audit_resume_quality(sample_audit_text, st.session_state.profile["skills"])

    c_ats1, c_ats2, c_ats3 = st.columns(3)
    c_ats1.metric("ATS Compatibility", f"{audit_res['ats_score']}/100")
    c_ats2.metric("Quantified Impact Score", f"{audit_res['impact_score']}/100", f"{audit_res['total_metrics']} metrics detected")
    c_ats3.metric("Action Verb Strength", f"{audit_res['action_verb_score']}/100", f"{len(audit_res['verbs_found'])} power verbs")

    st.subheader("💡 Actionable Improvement Recommendations")
    for tip in audit_res["tips"]:
        st.write(tip)

    # Role specific ATS keyword advice
    target_bench = ROLE_BENCHMARKS.get(active_role, {})
    missing_for_active = [sk for sk, _ in target_bench.items() if st.session_state.profile["skills"].get(sk, 0) < 5]
    if missing_for_active:
        st.info(f"🎯 **ATS Keyword Recommender for {active_role}:** Consider adding bullet points mentioning: **{', '.join(missing_for_active)}** to pass recruiter screening filters.")


# ==========================================
# PAGE 3: SKILL GAP & BENCHMARKS
# ==========================================
elif page == "⚖️ Skill Gap & Benchmarks":
    st.title(f"⚖️ Skill Gap Engine: {active_role}")
    st.markdown("Formula: **Priority Score = Importance × max(0, Target Level - Current Level)**")

    df_gap = pd.DataFrame(skill_gaps)
    st.dataframe(
        df_gap[["skill", "current_level", "target_level", "gap", "importance", "priority_score", "status"]],
        use_container_width=True
    )

    st.markdown("---")
    st.subheader("🛠️ Interactive Skill Proficiency Adjuster")
    st.markdown("Adjust your proficiency ratings (0 to 10) to simulate readiness improvements or test new skills.")

    all_current_skills = list(st.session_state.profile["skills"].keys())
    # Add benchmark skills if not present
    for s in req_benchmarks.keys():
        if s not in st.session_state.profile["skills"]:
            st.session_state.profile["skills"][s] = 0

    cols = st.columns(3)
    sorted_skills = sorted(st.session_state.profile["skills"].keys())
    for idx, skill in enumerate(sorted_skills):
        col = cols[idx % 3]
        with col:
            new_val = st.slider(
                f"{skill}",
                min_value=0,
                max_value=10,
                value=st.session_state.profile["skills"][skill],
                key=f"slider_{skill}"
            )
            st.session_state.profile["skills"][skill] = new_val


# ==========================================
# PAGE 4: JOB MATCH ENGINE
# ==========================================
elif page == "🔍 Job Match Engine":
    st.title("🔍 Job Description Matching Engine")
    st.markdown(f"Paste any Job Description (JD) to compute instant skill alignment with your profile for **{active_role}**.")

    jd_input = st.text_area(
        "Paste Target Job Description (JD):",
        height=220,
        placeholder="Example: We are looking for a Senior Generative AI Engineer proficient in Python, LangGraph, RAG architectures, FastAPI, Vector Databases, Docker, and Kubernetes..."
    )

    if st.button("🚀 Analyze Job Description Match", type="primary"):
        if jd_input.strip():
            extracted_reqs = JobDescriptionAnalyzer.extract_requirements(jd_input)
            match_res = CareerIntelligenceEngine.calculate_job_match(
                list(st.session_state.profile["skills"].keys()),
                extracted_reqs["required_skills"],
                extracted_reqs["preferred_skills"]
            )

            col_m1, col_m2 = st.columns([1, 2])
            with col_m1:
                st.metric("Job Match Score", f"{match_res['match_percentage']}%")
                if match_res['match_percentage'] >= 75:
                    st.success("🟢 Strong Candidate Fit")
                elif match_res['match_percentage'] >= 50:
                    st.warning("🟡 Moderate Fit — Address Missing Keywords")
                else:
                    st.error("🔴 Significant Gap — Upskilling Recommended")

            with col_m2:
                st.write(f"**✅ Matched Required Skills:** {', '.join(match_res['matched_required']) if match_res['matched_required'] else 'None detected'}")
                st.write(f"**⚠️ Missing Required Skills:** {', '.join(match_res['missing_required']) if match_res['missing_required'] else 'None! All covered'}")
                st.write(f"**🌟 Matched Preferred Skills:** {', '.join(match_res['matched_preferred']) if match_res['matched_preferred'] else 'None detected'}")
                st.write(f"**💡 Missing Preferred Skills:** {', '.join(match_res['missing_preferred']) if match_res['missing_preferred'] else 'None'}")


# ==========================================
# PAGE 5: PERSONALIZED ROADMAP
# ==========================================
elif page == "🗺️ Personalized Roadmap":
    st.title(f"🗺️ Adaptive Learning Roadmap: {active_role}")
    st.markdown(f"Customized sequential learning curriculum prioritizing your highest-gap skills for **{active_role}**.")

    roadmap = RoadmapService.generate_personalized_roadmap(skill_gaps)
    
    for step in roadmap:
        with st.container():
            st.markdown(f"### 📅 {step['timeframe']}: **{step['skill']}**")
            st.write(f"**Priority Score:** `{step['priority_score']}` | **Skill Gap:** `{step['gap']} pts`")
            st.info(f"**Curriculum Focus:** {step['focus']}")
            st.markdown("---")


# ==========================================
# PAGE 6: AI PORTFOLIO PROJECT GENERATOR
# ==========================================
elif page == "💡 AI Portfolio Project Generator":
    st.title("💡 AI Portfolio Project Generator & Blueprint Studio")
    st.markdown("Build high-signal, production-grade portfolio projects engineered to prove your competency and impress hiring managers.")

    tab1, tab2 = st.tabs(["🎯 Gap-Tailored Custom Project", "📚 Explore Full Project Library"])

    with tab1:
        st.subheader(f"🎯 Dynamic Project Blueprint for {active_role}")
        st.markdown("This project is algorithmically synthesized to bridge your top identified skill gaps.")

        top_gaps = [g for g in skill_gaps if g["gap"] > 0]
        if st.button("✨ Generate / Refresh Tailored Project Blueprint", type="primary"):
            st.session_state.active_project = ProjectGeneratorService.generate_project(active_role, top_gaps)

        if "active_project" not in st.session_state:
            st.session_state.active_project = ProjectGeneratorService.generate_project(active_role, top_gaps)

        proj = st.session_state.active_project

        st.markdown(f"## 🏆 {proj.title}")
        st.markdown(f"**Domain:** `{proj.domain}` | **Level:** `{proj.difficulty}` | **Estimated Effort:** `{proj.estimated_hours}`")
        st.info(proj.summary)

        st.markdown("#### 🛠️ Tech Stack & Key Skills Developed")
        st.write(" ".join([f"`{t}`" for t in proj.tech_stack]))
        st.markdown(f"**Skills Developed:** {', '.join(proj.skills_developed)}")

        c_arch, c_mile = st.columns(2)
        with c_arch:
            st.markdown("#### 🏗️ Architecture & Data Flow")
            st.code(proj.architecture_overview, language="text")

        with c_mile:
            st.markdown("#### 📋 Milestone-by-Milestone Implementation")
            for m in proj.milestones:
                st.markdown(f"- {m}")

        st.markdown("#### 💼 High-Impact Resume Bullets (STAR Format)")
        for b in proj.resume_bullet_points:
            st.markdown(f"> - {b}")

        st.markdown("#### 🎙️ Anticipated Interview Questions & Discussion Points")
        for q in proj.sample_interview_questions:
            st.markdown(f"- ❓ **{q}**")

        if proj.production_gotchas:
            st.markdown("#### ⚠️ Production Gotchas & System Challenges")
            for gotcha in proj.production_gotchas:
                st.warning(gotcha)

        with st.expander("📄 Export GitHub README Markdown Template"):
            readme_md = ProjectGeneratorService.generate_github_readme(proj)
            st.text_area("Copy GitHub README.md", value=readme_md, height=250)

    with tab2:
        st.subheader("📚 Multi-Domain Production Project Library")
        st.markdown("Browse curated enterprise-grade projects across different disciplines and difficulty tiers.")

        f_col1, f_col2, f_col3 = st.columns(3)
        with f_col1:
            all_roles_filter = ["All Roles"] + list(ROLE_BENCHMARKS.keys())
            f_role = st.selectbox("Filter by Role Category", all_roles_filter)
        with f_col2:
            f_diff = st.selectbox("Filter by Difficulty", ["All Difficulties", "Intermediate / Applied", "Advanced / Enterprise"])
        with f_col3:
            f_dom = st.selectbox("Filter by Domain", ["All Domains", "Fintech", "Developer Tools", "E-Commerce", "Big Data", "DevOps", "Healthcare", "Industrial"])

        filtered_projects = ProjectGeneratorService.filter_projects(
            role_category=f_role,
            difficulty=f_diff,
            domain=f_dom
        )

        st.write(f"Showing **{len(filtered_projects)}** matching project blueprints:")

        for idx, p in enumerate(filtered_projects):
            with st.expander(f"🚀 {p.title} ({p.role_category} | {p.difficulty})"):
                st.markdown(f"**Domain:** `{p.domain}` | **Effort:** `{p.estimated_hours}`")
                st.write(p.summary)
                st.markdown(f"**Tech Stack:** {' '.join([f'`{t}`' for t in p.tech_stack])}")
                
                col_p1, col_p2 = st.columns(2)
                with col_p1:
                    st.markdown("**🏗️ Architecture:**")
                    st.text(p.architecture_overview)
                with col_p2:
                    st.markdown("**📋 Milestones:**")
                    for m in p.milestones:
                        st.markdown(f"- {m}")

                st.markdown("**💼 Resume Bullet Points:**")
                for b in p.resume_bullet_points:
                    st.markdown(f"> - {b}")

                st.markdown("**🎙️ Sample Interview Questions:**")
                for q in p.sample_interview_questions:
                    st.markdown(f"- {q}")


# ==========================================
# PAGE 7: MOCK INTERVIEW SIMULATOR
# ==========================================
elif page == "🎙️ Mock Interview Simulator":
    st.title(f"🎙️ AI Mock Interview Simulation: {active_role}")
    st.markdown(f"Practice role-specific technical and architectural interview questions tailored for **{active_role}**.")

    questions = MockInterviewService.get_interview_suite(active_role)
    q_titles = [f"Q{q['id']}: {q['type']}" for q in questions]
    selected_idx = st.selectbox("Select Interview Question", range(len(questions)), format_func=lambda i: q_titles[i])
    selected_q = questions[selected_idx]

    st.info(f"### ❓ Question:\n\n{selected_q['question']}")
    st.caption(f"**Evaluator Rubric:** {selected_q['rubric']}")

    user_response = st.text_area(
        "Your Response:",
        height=180,
        placeholder="Explain your architectural design, metric benchmarks, system trade-offs, and STAR methodology outcomes..."
    )

    if st.button("🚀 Submit & Score Answer", type="primary"):
        if user_response.strip():
            with st.spinner("Analyzing answer depth, metrics, and technical articulation..."):
                eval_res = MockInterviewService.evaluate_response(user_response)
                
                c1, c2, c3 = st.columns(3)
                c1.metric("Overall Score", f"{eval_res['overall_score']}%")
                c2.metric("Technical Depth", f"{eval_res['technical_score']}%")
                c3.metric("Communication & Structure", f"{eval_res['communication_score']}%")

                st.subheader("📋 Detailed Evaluator Feedback")
                for item in eval_res["feedback"]:
                    st.write(item)

                db = get_db()
                session_rec = InterviewSession(
                    role=active_role,
                    question=selected_q["question"],
                    user_answer=user_response,
                    overall_score=eval_res["overall_score"],
                    technical_score=eval_res["technical_score"],
                    communication_score=eval_res["communication_score"],
                    problem_solving_score=eval_res["problem_solving_score"],
                    behavioral_score=eval_res["behavioral_score"]
                )
                db.add(session_rec)
                db.commit()
                st.success("🎉 Interview response recorded in local database!")
        else:
            st.warning("Please enter your response before submitting.")


# ==========================================
# PAGE 8: JOB APPLICATION TRACKER
# ==========================================
elif page == "📋 Job Application Tracker":
    st.title("📋 Job Application Tracker")
    st.markdown("Track and manage your applications, interview stages, match scores, and recruiter follow-ups.")

    with st.expander("➕ Log New Job Application", expanded=False):
        with st.form("job_form"):
            c_f1, c_f2 = st.columns(2)
            with c_f1:
                comp = st.text_input("Company Name", placeholder="e.g. Google, Anthropic, Stripe")
                role_input = st.text_input("Role Title", value=active_role)
            with c_f2:
                status = st.selectbox("Application Status", ["Applied", "Screening", "Technical Interview", "Onsite / Final", "Offer", "Rejected"])
                salary = st.text_input("Target Salary / Range", placeholder="e.g. $140,000 - $170,000")
            
            notes = st.text_area("Notes & Interview Prep Reminders", placeholder="Key interviewers, recruiter emails, architecture topics...")
            submitted = st.form_submit_button("Save Application", type="primary")

            if submitted and comp and role_input:
                db = get_db()
                new_job = JobApplication(
                    company=comp,
                    role=role_input,
                    status=status,
                    salary_range=salary,
                    match_score=readiness,
                    notes=notes
                )
                db.add(new_job)
                db.commit()
                st.success(f"Application for **{comp}** ({role_input}) logged successfully!")
                st.rerun()

    db = get_db()
    jobs = db.query(JobApplication).all()
    if jobs:
        st.subheader(f"Tracked Applications ({len(jobs)})")
        df_jobs = pd.DataFrame([{
            "ID": j.id,
            "Company": j.company,
            "Role": j.role,
            "Status": j.status,
            "Match %": f"{j.match_score:.1f}%" if j.match_score else "N/A",
            "Salary Range": j.salary_range or "N/A",
            "Date Applied": j.applied_date.strftime("%Y-%m-%d"),
            "Notes": j.notes or ""
        } for j in jobs])
        st.dataframe(df_jobs, use_container_width=True)
    else:
        st.info("No job applications logged yet. Click 'Log New Job Application' above to start tracking your search.")
