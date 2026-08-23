from models import ProjectBlueprint
from typing import Dict, List, Optional
import random

CURATED_PROJECTS: List[ProjectBlueprint] = [
    # --- Generative AI & Agentic Systems ---
    ProjectBlueprint(
        title="Enterprise Multi-Agent Financial Due Diligence & SEC Filing Auditor",
        role_category="Generative AI Engineer",
        difficulty="Advanced / Enterprise",
        domain="Fintech & Hedge Funds",
        estimated_hours="50-70 Hours",
        summary="An autonomous agentic platform that ingests 100+ page SEC 10-K filings, performs hybrid dense/sparse vector search with reranking, and orchestrates verification agents to detect balance sheet anomalies and revenue discrepancies.",
        tech_stack=["Python", "LangGraph", "ChromaDB", "FastAPI", "Streamlit", "Docker", "Cohere Rerank"],
        skills_developed=["LangGraph", "RAG", "AI Agents", "FastAPI", "Vector Databases", "System Design"],
        architecture_overview="1. Ingestion: PyMuPDF + unstructured parsing of balance sheets and tables.\n2. Hybrid Retrieval: ChromaDB dense vector indexing + BM25 keyword reranking.\n3. Orchestrator: LangGraph StateGraph with Supervisor, Auditor, and Validator agents.\n4. Microservice: FastAPI with SSE streaming & structured Pydantic response validation.",
        milestones=[
            "Milestone 1: PDF Table Extraction & Semantic Parent-Child Chunking",
            "Milestone 2: Hybrid RAG Pipeline with Cross-Encoder Reranking & Cohere API",
            "Milestone 3: LangGraph Multi-Agent State Machine with Cyclic Validation & Error Fallbacks",
            "Milestone 4: Async FastAPI Backend with WebSocket/SSE Streaming & Docker Containerization"
        ],
        resume_bullet_points=[
            "Architected an autonomous multi-agent financial auditing engine using LangGraph and FastAPI, reducing manual SEC 10-K analysis time by 78%.",
            "Engineered a hybrid retrieval system with ChromaDB and Cohere Cross-Encoder, improving citation precision and table retrieval accuracy by 38%."
        ],
        sample_interview_questions=[
            "How did you mitigate hallucinations and circular loops in the multi-agent graph?",
            "Why did you choose hybrid sparse-dense search over standard cosine similarity vector search?"
        ],
        production_gotchas=[
            "Token context limits when feeding multiple 10-K tables; solved via summary indexing.",
            "Agent looping when verification fails; resolved with maximum recursion depth guards."
        ]
    ),
    ProjectBlueprint(
        title="Self-Correcting Autonomous Coding & Refactoring Agent",
        role_category="Generative AI Engineer",
        difficulty="Advanced / Enterprise",
        domain="Developer Tools & Infrastructure",
        estimated_hours="45-60 Hours",
        summary="An AI software engineer bot that analyzes GitHub repositories, generates unit tests, runs test suites inside sandboxed Docker containers, and recursively debugs code until all tests pass.",
        tech_stack=["Python", "LangGraph", "Docker SDK", "GitPython", "OpenAI / Claude API", "FastAPI"],
        skills_developed=["AI Agents", "Docker", "System Design", "Python", "LLMs"],
        architecture_overview="1. Code Ingestion: Tree-sitter AST parsing + Git diff generation.\n2. Execution Sandbox: Isolated Docker runtime executing pytest and linting.\n3. Reflection Loop: LLM critiques stderr output and edits target AST nodes.\n4. CI Integration: Creates pull request with benchmark summary.",
        milestones=[
            "Milestone 1: AST Parser and Repository Dependency Graph Builder",
            "Milestone 2: Sandboxed Docker Test Execution Runtime with Timeout Guards",
            "Milestone 3: Recursive Reflection & Patch Synthesis Engine in LangGraph",
            "Milestone 4: Automated GitHub PR & Benchmark Dashboard"
        ],
        resume_bullet_points=[
            "Developed a sandboxed autonomous refactoring agent that automatically resolved 64% of failing repository test suites using recursive LLM self-correction.",
            "Integrated Docker SDK container isolation, preventing unsafe arbitrary code execution during automated unit testing."
        ],
        sample_interview_questions=[
            "How do you ensure security when executing LLM-generated code in your backend?",
            "How did you manage prompt context size when parsing large code repositories?"
        ]
    ),
    ProjectBlueprint(
        title="Real-Time Multimodal Voice & Video Customer Support AI",
        role_category="Generative AI Engineer",
        difficulty="Intermediate / Applied",
        domain="E-Commerce & SaaS",
        estimated_hours="35-45 Hours",
        summary="A low-latency real-time voice assistant with vision capabilities that screen-shares with users, diagnoses UI issues, and speaks back with sub-500ms voice latency using WebSockets.",
        tech_stack=["Python", "FastAPI", "WebRTC / WebSockets", "OpenAI Realtime API", "Whisper", "React"],
        skills_developed=["FastAPI", "System Design", "LLMs", "React / Next.js", "Python"],
        architecture_overview="1. Client: React WebRTC capture for bidirectional audio & screen stream.\n2. Gateway: FastAPI WebSocket handler for chunked Opus audio forwarding.\n3. Model: OpenAI Realtime / Deepgram speech-to-speech with function-calling triggers.\n4. Tool Engine: Autonomous DB lookup and ticketing integration.",
        milestones=[
            "Milestone 1: WebRTC / WebSocket Audio Streaming Infrastructure",
            "Milestone 2: Function Calling Protocol for CRM & Ticket Resolution",
            "Milestone 3: Sub-500ms End-to-End Latency Optimization & VAD (Voice Activity Detection)",
            "Milestone 4: React UI with Live Audio Visualizer & Transcript Feed"
        ],
        resume_bullet_points=[
            "Engineered a real-time multimodal voice support copilot achieving sub-450ms turnaround latency via streaming WebSockets and Whisper VAD.",
            "Integrated tool-calling capabilities to autonomously query inventory databases and resolve 40% of tier-1 support inquiries."
        ],
        sample_interview_questions=[
            "How did you minimize round-trip voice latency over WebSockets?",
            "How did you handle interruptions when the user speaks while the bot is answering?"
        ]
    ),

    # --- Machine Learning & Deep Learning ---
    ProjectBlueprint(
        title="Real-Time Fraud & Anomaly Detection Engine with Graph Neural Networks",
        role_category="Machine Learning Engineer",
        difficulty="Advanced / Enterprise",
        domain="Fintech & Payments",
        estimated_hours="50-65 Hours",
        summary="An end-to-end payment fraud detection system combining XGBoost tabular models and PyTorch Geometric Graph Neural Networks (GNNs) to identify coordinated money laundering rings in streaming transactions.",
        tech_stack=["Python", "PyTorch Geometric", "XGBoost", "Kafka", "Redis", "Docker", "FastAPI"],
        skills_developed=["PyTorch", "Machine Learning", "Deep Learning", "MLOps", "Docker", "SQL"],
        architecture_overview="1. Stream Ingestion: Apache Kafka event broker ingesting 5,000 transactions/sec.\n2. Feature Store: Redis in-memory cache for sliding window aggregations.\n3. Hybrid Model: XGBoost for transaction features + PyG GNN for graph neighborhood risk.\n4. Serving: TorchScript + FastAPI with <20ms inference latency.",
        milestones=[
            "Milestone 1: Synthetic Financial Transaction Graph Generation & Feature Engineering",
            "Milestone 2: PyTorch Geometric GNN & XGBoost Ensemble Training Pipeline",
            "Milestone 3: Kafka & Redis Streaming Ingestion with Sliding-Window Velocity Features",
            "Milestone 4: High-Throughput FastAPI Serving (<20ms P99 latency) with Prometheus Metrics"
        ],
        resume_bullet_points=[
            "Engineered a hybrid GNN + XGBoost fraud detection pipeline processing 5K QPS with sub-20ms P99 inference latency.",
            "Increased fraud recall by 26% compared to legacy rule-based systems while reducing false positive alerts by 19%."
        ],
        sample_interview_questions=[
            "Why combine Graph Neural Networks with traditional GBDTs like XGBoost?",
            "How did you handle extreme class imbalance in fraud data (e.g. 0.05% positive rate)?"
        ]
    ),
    ProjectBlueprint(
        title="Deep Reinforcement Learning Portfolio Optimizer & Trading Strategy",
        role_category="Machine Learning Engineer",
        difficulty="Intermediate / Applied",
        domain="Fintech & Quantitative Finance",
        estimated_hours="40-50 Hours",
        summary="A PPO (Proximal Policy Optimization) reinforcement learning agent trained in an OpenAI Gym custom environment to dynamically rebalance a multi-asset crypto/equity portfolio under transaction cost constraints.",
        tech_stack=["Python", "PyTorch", "Stable-Baselines3", "Gymnasium", "Pandas", "Plotly"],
        skills_developed=["Deep Learning", "PyTorch", "Machine Learning", "Pandas", "Python"],
        architecture_overview="1. Data Pipeline: Yahoo Finance / Polygon historical tick data extraction.\n2. Gym Environment: Custom multi-asset order execution engine with slippage & fees.\n3. Policy Agent: Actor-Critic PPO network with LSTM feature extractor.\n4. Evaluation: Sharpe ratio, max drawdown, and backtesting comparison vs S&P 500.",
        milestones=[
            "Milestone 1: High-Fidelity Gymnasium Market Simulation with Slippage Modeling",
            "Milestone 2: PPO Actor-Critic Policy Network with Temporal Attention Layers",
            "Milestone 3: Hyperparameter Tuning via Optuna across 500+ Simulated Market Regimes",
            "Milestone 4: Interactive Plotly Backtest Dashboard with Risk Metric Visualizers"
        ],
        resume_bullet_points=[
            "Trained a deep reinforcement learning agent (PPO) achieving a 1.84 Sharpe Ratio across 5 years of out-of-sample backtested market data.",
            "Designed a custom Gymnasium environment simulating realistic order book slippage and trading fees."
        ],
        sample_interview_questions=[
            "How did you prevent the RL agent from overfitting to historical market regimes?",
            "What reward function design produced the most stable Sharpe ratio?"
        ]
    ),

    # --- Data Science & Analytics ---
    ProjectBlueprint(
        title="Customer Lifetime Value (LTV) & Uplift Modeling Engine with Causal Inference",
        role_category="Data Scientist",
        difficulty="Intermediate / Applied",
        domain="E-Commerce & Marketing",
        estimated_hours="30-40 Hours",
        summary="A statistical and machine learning platform predicting individual customer lifetime value and evaluating promotional treatment uplift using causal trees (DoWhy / CausalML) for targeted marketing spend.",
        tech_stack=["Python", "SQL", "Pandas", "CausalML", "Scikit-Learn", "Streamlit", "Plotly"],
        skills_developed=["Statistics & Probability", "A/B Testing", "Machine Learning", "SQL", "Pandas", "Data Visualization"],
        architecture_overview="1. Data Extraction: Complex SQL cohort queries joining transactions, sessions, and retention.\n2. Probabilistic Modeling: BG/NBD and Gamma-Gamma models for repeat purchase behavior.\n3. Causal Uplift: T-Learner / X-Learner to isolate true promotional incrementality.\n4. UI: Executive scenario simulation tool.",
        milestones=[
            "Milestone 1: SQL Data Warehouse Modeling for Retention & RFM Segmentation",
            "Milestone 2: BG/NBD & Gamma-Gamma Probabilistic LTV Estimation",
            "Milestone 3: Two-Model Uplift Strategy (CausalML) to Identify Persuadables",
            "Milestone 4: Interactive What-If ROI Calculator in Streamlit"
        ],
        resume_bullet_points=[
            "Built a causal uplift & LTV modeling suite identifying top 15% persuadable customers, projecting a 22% increase in marketing campaign ROI.",
            "Developed complex SQL cohort models and BG/NBD probabilistic frameworks to forecast 12-month customer retention."
        ],
        sample_interview_questions=[
            "What is the difference between standard churn prediction and causal uplift modeling?",
            "How do you design an A/B test when network effects or sample interference are present?"
        ]
    ),

    # --- Data Engineering ---
    ProjectBlueprint(
        title="Petabyte-Scale Real-Time Clickstream Lakehouse with Apache Spark & Iceberg",
        role_category="Data Engineer",
        difficulty="Advanced / Enterprise",
        domain="Big Data & Cloud Infrastructure",
        estimated_hours="45-60 Hours",
        summary="A production-ready data streaming lakehouse ingesting billions of web events via Kafka, transforming data using Spark Structured Streaming, and writing ACID transactions into Apache Iceberg tables on Cloud Storage.",
        tech_stack=["Python", "Apache Spark", "Apache Iceberg", "Kafka", "Airflow", "Docker", "PostgreSQL", "dbt"],
        skills_developed=["Spark", "Data Pipelines", "SQL", "Kafka", "Airflow", "Cloud Data Warehouse", "System Design"],
        architecture_overview="1. Ingestion: Distributed Kafka cluster with Schema Registry.\n2. Streaming: PySpark Structured Streaming with watermarking & deduplication.\n3. Lakehouse: Apache Iceberg with ACID snapshot isolation & partition evolution.\n4. Orchestration: Airflow DAGs for table compaction and dbt dimensional modeling.",
        milestones=[
            "Milestone 1: Dockerized Kafka & Avro Schema Registry Cluster Setup",
            "Milestone 2: PySpark Streaming Pipeline with 10-minute Watermarking & Exactly-Once Semantics",
            "Milestone 3: Apache Iceberg Lakehouse Integration with Dynamic Partition Pruning",
            "Milestone 4: Airflow Orchestrated dbt Star-Schema Transformations & Data Quality Tests"
        ],
        resume_bullet_points=[
            "Architected a real-time event streaming lakehouse using Spark Structured Streaming and Apache Iceberg, processing 10M+ events/hour with zero data loss.",
            "Implemented automated Iceberg compaction and dbt data quality assertions, cutting analytical query costs by 42%."
        ],
        sample_interview_questions=[
            "How do you handle late-arriving events in Spark Structured Streaming?",
            "What advantages does Apache Iceberg provide over traditional Hive table formats?"
        ]
    ),

    # --- MLOps & Platform Engineering ---
    ProjectBlueprint(
        title="Enterprise Self-Healing LLM Gateway with Semantic Caching & Fallbacks",
        role_category="MLOps Engineer",
        difficulty="Advanced / Enterprise",
        domain="DevOps & Platform Engineering",
        estimated_hours="40-55 Hours",
        summary="A high-performance LLM proxy gateway with Redis semantic vector caching, intelligent multi-provider load balancing (OpenAI, Anthropic, Ollama), rate-limit retry circuits, and OpenTelemetry tracing.",
        tech_stack=["Python", "FastAPI", "Redis", "Docker", "Kubernetes", "Prometheus", "Grafana", "MLflow"],
        skills_developed=["MLOps", "Docker", "Kubernetes", "CI/CD", "Model Monitoring", "System Design"],
        architecture_overview="1. Proxy: Async FastAPI reverse proxy intercepting OpenAI-compatible chat requests.\n2. Semantic Cache: Redis Vector Similarity Search returning cached responses for >0.92 cosine similarity.\n3. Resilience: Token bucket rate limiter + circuit breaker cascading to local Ollama fallback.\n4. Observability: Prometheus metrics + Grafana dashboard tracking P99 latency, cost, and tokens.",
        milestones=[
            "Milestone 1: FastAPI Reverse Proxy with Dynamic Provider Routing & Secret Management",
            "Milestone 2: Redis Vector Semantic Cache (saving up to 40% LLM API expenses)",
            "Milestone 3: Circuit Breaker & Automatic Failover Engine with Exponential Backoff",
            "Milestone 4: Kubernetes Helm Deployment with Prometheus & Grafana Monitoring"
        ],
        resume_bullet_points=[
            "Engineered a production LLM proxy gateway with Redis semantic caching, reducing API expenditure by 35% and shaving 300ms off average response latency.",
            "Deployed multi-region Kubernetes Helm charts with automated Prometheus alerts and circuit-breaking fallbacks."
        ],
        sample_interview_questions=[
            "How does semantic caching differ from exact-match Redis caching for LLMs?",
            "How do you monitor model drift and hallucination rates in live production traffic?"
        ]
    ),

    # --- Computer Vision & Edge AI ---
    ProjectBlueprint(
        title="Edge AI Real-Time Multi-Object Tracking & PPE Safety Compliance System",
        role_category="Computer Vision Engineer",
        difficulty="Intermediate / Applied",
        domain="Industrial & IoT",
        estimated_hours="40-50 Hours",
        summary="A real-time edge vision pipeline running YOLOv8 + ByteTrack to detect workers, hard hats, safety vests, and hazardous machinery zones with 30 FPS inference on NVIDIA TensorRT / Jetson.",
        tech_stack=["Python", "PyTorch", "OpenCV", "YOLOv8", "TensorRT", "FastAPI", "Docker"],
        skills_developed=["OpenCV", "PyTorch", "Deep Learning", "Object Detection", "Edge AI / TensorRT", "Python"],
        architecture_overview="1. Video Capture: RTSP camera stream decoding via OpenCV GStreamer.\n2. Model: YOLOv8 custom fine-tuned on safety PPE dataset & compiled to TensorRT FP16 engine.\n3. Tracker: ByteTrack algorithm assigning persistent IDs across video frames.\n4. Alerting: Real-time zone intrusion triggers pushing alerts via WebSockets.",
        milestones=[
            "Milestone 1: Custom PPE Dataset Annotation & Data Augmentation Pipeline",
            "Milestone 2: YOLOv8 Model Training with Transfer Learning in PyTorch",
            "Milestone 3: TensorRT FP16 Engine Optimization (boosting FPS from 14 to 45 FPS)",
            "Milestone 4: ByteTrack Multi-Camera Tracking & Event Notification Dashboard"
        ],
        resume_bullet_points=[
            "Deployed an Edge AI safety compliance system running at 45 FPS using TensorRT FP16 optimization on live RTSP video feeds.",
            "Achieved 94.2% mAP@0.5 on custom PPE hazard detection using fine-tuned YOLOv8 and ByteTrack."
        ],
        sample_interview_questions=[
            "How does TensorRT quantization (FP16/INT8) accelerate inference speed on edge hardware?",
            "How does ByteTrack resolve occlusion issues compared to traditional SORT / DeepSORT?"
        ]
    ),

    # --- NLP & LLM Engineer ---
    ProjectBlueprint(
        title="Domain-Adapted Medical LLM with LoRA Fine-Tuning & Factuality Guardrails",
        role_category="NLP & LLM Engineer",
        difficulty="Advanced / Enterprise",
        domain="Healthcare & Biotech",
        estimated_hours="45-60 Hours",
        summary="A specialized clinical question-answering assistant built by fine-tuning Llama-3 8B on PubMed / MIMIC clinical dialogue with QLoRA, coupled with NeMo Guardrails to prevent medical misinformation.",
        tech_stack=["Python", "Transformers", "PEFT / QLoRA", "PyTorch", "vLLM", "NeMo Guardrails", "FastAPI"],
        skills_developed=["Fine-Tuning / LoRA", "Transformers", "LLMs", "PyTorch", "Prompt Engineering", "Python"],
        architecture_overview="1. Dataset Prep: Tokenized medical QA pairs with instruction formatting.\n2. QLoRA Training: 4-bit quantized parameter-efficient fine-tuning on 2x A10G GPUs.\n3. Evaluation: ROUGE, BLEU, and LLM-as-a-judge factuality metrics against medical benchmarks.\n4. Guardrails: NeMo Guardrails ensuring responses include appropriate clinical disclaimers.",
        milestones=[
            "Milestone 1: Biomedical Corpus Cleansing, Deduplication & ChatML Formatting",
            "Milestone 2: QLoRA Fine-Tuning with Unsloth / Hugging Face PEFT on Llama-3",
            "Milestone 3: Automated Factuality & Hallucination Benchmark with MedQA Evaluation",
            "Milestone 4: High-Throughput Serving with vLLM & NeMo Safety Rails"
        ],
        resume_bullet_points=[
            "Fine-tuned a domain-adapted 8B LLM using QLoRA, improving MedQA diagnostic accuracy by 24% over the base foundation model.",
            "Deployed vLLM serving with PagedAttention and safety guardrails, supporting 80 concurrent users with 3.2x throughput."
        ],
        sample_interview_questions=[
            "What are the trade-offs between RAG and domain-specific LoRA fine-tuning for specialized corpora?",
            "Explain how PagedAttention in vLLM mitigates GPU memory fragmentation during token generation."
        ]
    ),

    # --- Full-Stack AI Engineer ---
    ProjectBlueprint(
        title="AI Document Intelligence Studio: Next.js + FastAPI Multi-Doc Copilot",
        role_category="Full-Stack AI Engineer",
        difficulty="Intermediate / Applied",
        domain="Enterprise Productivity & Legal",
        estimated_hours="35-45 Hours",
        summary="A modern web app allowing users to upload PDFs, spreadsheets, and Word docs, highlight passages, perform grounded Q&A with citations, and export AI-generated research summaries.",
        tech_stack=["Next.js", "TypeScript", "FastAPI", "Python", "ChromaDB", "Tailwind CSS", "Docker"],
        skills_developed=["React / Next.js", "TypeScript", "FastAPI", "LLM Integration", "Docker", "Vector Databases"],
        architecture_overview="1. Frontend: Next.js 14 App Router with Tailwind CSS, PDF.js viewer, and Zustand state.\n2. Backend: FastAPI REST API with async background Celery worker for doc parsing.\n3. Embedding: FastEmbed local embeddings stored in ChromaDB.\n4. Streaming: Server-Sent Events (SSE) streaming tokens directly to UI with interactive citation markers.",
        milestones=[
            "Milestone 1: Next.js Responsive UI with Interactive PDF Viewer & Citation Highlighting",
            "Milestone 2: FastAPI Document Parsing & Semantic Chunking Service",
            "Milestone 3: Grounded Vector Search Pipeline with Bounding Box Citation Coordinates",
            "Milestone 4: Multi-Tenant Authentication & Cloud S3 File Storage Integration"
        ],
        resume_bullet_points=[
            "Built a full-stack document intelligence platform (Next.js 14 + FastAPI) with grounded citations, serving 500+ daily active users.",
            "Engineered an SSE streaming response pipeline delivering sub-200ms time-to-first-token for long-form synthesis."
        ],
        sample_interview_questions=[
            "How do you synchronize UI highlight coordinates with vector search citation chunks?",
            "How do you handle background processing for huge multi-hundred page PDF uploads?"
        ]
    )
]

class ProjectGeneratorService:
    @staticmethod
    def get_all_projects() -> List[ProjectBlueprint]:
        return CURATED_PROJECTS

    @staticmethod
    def filter_projects(
        role_category: Optional[str] = None,
        difficulty: Optional[str] = None,
        domain: Optional[str] = None
    ) -> List[ProjectBlueprint]:
        results = CURATED_PROJECTS
        if role_category and role_category != "All Roles":
            results = [p for p in results if role_category.lower() in p.role_category.lower()]
        if difficulty and difficulty != "All Difficulties":
            results = [p for p in results if difficulty.lower() in p.difficulty.lower()]
        if domain and domain != "All Domains":
            results = [p for p in results if domain.lower() in p.domain.lower()]
        return results

    @staticmethod
    def generate_project(target_role: str, top_gaps: List[Dict]) -> ProjectBlueprint:
        # Check if there is a curated project matching the target role
        matching = [p for p in CURATED_PROJECTS if target_role.lower() in p.role_category.lower() or p.role_category.lower() in target_role.lower()]
        
        gaps_list = [g["skill"] for g in top_gaps if g.get("gap", 0) > 0][:4]
        if not gaps_list:
            gaps_list = ["System Design", "Cloud Architecture", "Docker", "Python"]

        if matching:
            base = matching[0]
            # Adapt base project with candidate's specific gap skills
            return ProjectBlueprint(
                title=base.title,
                role_category=target_role,
                difficulty=base.difficulty,
                domain=base.domain,
                estimated_hours=base.estimated_hours,
                summary=base.summary,
                tech_stack=list(set(base.tech_stack + gaps_list[:2])),
                skills_developed=list(set(base.skills_developed + gaps_list)),
                architecture_overview=base.architecture_overview,
                milestones=base.milestones,
                resume_bullet_points=base.resume_bullet_points,
                sample_interview_questions=base.sample_interview_questions,
                production_gotchas=base.production_gotchas
            )
        
        # Generic tailored project for any custom role
        title = f"Production-Grade Enterprise {target_role} Acceleration Platform"
        return ProjectBlueprint(
            title=title,
            role_category=target_role,
            difficulty="Advanced / Enterprise",
            domain="Enterprise Cloud & AI Services",
            estimated_hours="45-60 Hours",
            summary=f"A scalable, production-tested end-to-end platform engineered to bridge core industry requirements for modern {target_role} positions, demonstrating mastery of {', '.join(gaps_list[:3])}.",
            tech_stack=["Python", "Docker", "FastAPI", "PostgreSQL", "Cloud (AWS/GCP)"] + gaps_list[:3],
            skills_developed=gaps_list,
            architecture_overview=f"1. Core Engine: Microservice architecture incorporating {gaps_list[0] if gaps_list else 'modern frameworks'}.\n2. Data Layer: High-performance storage and caching.\n3. Serving Layer: Asynchronous API endpoints with structured validation.\n4. CI/CD: Automated containerized testing and deployment.",
            milestones=[
                f"Milestone 1: Core Architecture & Data Pipeline Setup ({gaps_list[0] if gaps_list else 'Foundation'})",
                f"Milestone 2: Advanced Feature Implementation with {gaps_list[1] if len(gaps_list) > 1 else 'Scalable Design'}",
                "Milestone 3: Benchmark Testing, Latency Optimization & Metric Collection",
                "Milestone 4: Docker Containerization, CI/CD Pipeline & Documentation"
            ],
            resume_bullet_points=[
                f"Architected an end-to-end {target_role} solution utilizing {gaps_list[0] if gaps_list else 'Python'} and Docker, reducing operational overhead by 40%.",
                f"Engineered high-throughput service components, improving processing speed and system reliability by 35%."
            ],
            sample_interview_questions=[
                f"How did you structure the architecture to effectively integrate {gaps_list[0] if gaps_list else 'the core tech'}?",
                "What architectural trade-offs did you consider regarding latency vs throughput?"
            ],
            production_gotchas=[
                "Managing connection pools and memory leaks under heavy concurrent traffic.",
                "Ensuring robust schema versioning and backward compatibility."
            ]
        )

    @staticmethod
    def generate_github_readme(project: ProjectBlueprint) -> str:
        tech_badges = " ".join([f"`{t}`" for t in project.tech_stack])
        skills_bullets = "\n".join([f"- **{s}**" for s in project.skills_developed])
        milestone_text = "\n".join([f"- [ ] {m}" for m in project.milestones])
        resume_text = "\n".join([f"> - {r}" for r in project.resume_bullet_points])

        return f"""# 🚀 {project.title}

> **Domain**: {project.domain} | **Level**: {project.difficulty} | **Estimated Effort**: {project.estimated_hours}

## 📖 Executive Summary
{project.summary}

## 🛠️ Tech Stack & Dependencies
{tech_badges}

## 🎯 Key Skills Demonstrated
{skills_bullets}

## 🏗️ System Architecture & Data Flow
```text
{project.architecture_overview}
```

## 📋 Implementation Roadmap & Milestones
{milestone_text}

## 💼 High-Impact Resume Bullets (STAR Format)
{resume_text}

## 🎙️ Sample Interview Talking Points & Questions
{chr(10).join([f"- **Q: {q}**" for q in project.sample_interview_questions])}

---
*Generated by AI Career Coach Portfolio Engine*
"""
