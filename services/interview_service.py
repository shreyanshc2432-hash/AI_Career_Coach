from typing import Dict, List, Any

ROLE_INTERVIEWS: Dict[str, List[Dict[str, Any]]] = {
    "Generative AI Engineer": [
        {
            "id": 1,
            "type": "System Design & Latency",
            "question": "How do you optimize latency and handle memory constraints when serving a low-latency LLM or RAG pipeline in production?",
            "rubric": "Evaluates quantization (AWQ/GPTQ), asynchronous token streaming, semantic caching, vector index pruning, and reranking trade-offs."
        },
        {
            "id": 2,
            "type": "Agentic Architecture",
            "question": "Explain how you design a multi-agent system with cyclic state graphs in LangGraph, and how you prevent infinite loops or tool hallucinations.",
            "rubric": "Evaluates state schema design, supervisor patterns, recursion limits, deterministic fallback policies, and tool output validation."
        }
    ],
    "Machine Learning Engineer": [
        {
            "id": 1,
            "type": "Production ML Architecture",
            "question": "How do you design a real-time feature store and model inference service that handles 10,000 QPS with sub-20ms latency?",
            "rubric": "Evaluates in-memory caching (Redis/Feast), asynchronous feature retrieval, batching (Triton/TorchScript), and horizontal autoscaling."
        },
        {
            "id": 2,
            "type": "Model Drift & Monitoring",
            "question": "How do you detect concept drift and data covariate shift in production ML models, and what is your automated retraining strategy?",
            "rubric": "Evaluates PSI, KS tests, Wasserstein distance, shadow deployments, and canary rollback strategies."
        }
    ],
    "Data Scientist": [
        {
            "id": 1,
            "type": "Causal Inference & Experimentation",
            "question": "How do you design an A/B test when there is significant network spillover between the control and treatment groups?",
            "rubric": "Evaluates cluster randomization, synthetic control methods, difference-in-differences, and switchback designs."
        }
    ],
    "Data Engineer": [
        {
            "id": 1,
            "type": "Distributed Streaming",
            "question": "How do you guarantee exactly-once processing and handle late-arriving out-of-order records in an Apache Spark streaming pipeline with Kafka?",
            "rubric": "Evaluates watermarking, checkpointing, idempotent writes, transactional state stores, and dead-letter queues."
        }
    ],
    "MLOps Engineer": [
        {
            "id": 1,
            "type": "CI/CD & Model Governance",
            "question": "Describe an end-to-end CI/CD pipeline for deploying ML models to Kubernetes, including automated validation gates, Canary rollouts, and rollback triggers.",
            "rubric": "Evaluates GitOps (ArgoCD), automated shadow inference, Prometheus metric thresholding, and Helm packaging."
        }
    ],
    "AI Solutions Architect": [
        {
            "id": 1,
            "type": "Enterprise AI Strategy & Security",
            "question": "How do you architect an enterprise-wide generative AI platform that complies with SOC2, GDPR, and prevents prompt injection and data leakage?",
            "rubric": "Evaluates tenant isolation, VPC peering, PII redaction filters, semantic guardrails, RBAC, and audit logging."
        }
    ],
    "Computer Vision Engineer": [
        {
            "id": 1,
            "type": "Edge Optimization & Detection",
            "question": "How do you optimize an object detection model (e.g. YOLO) for deployment on edge devices with strict power and memory budgets?",
            "rubric": "Evaluates TensorRT FP16/INT8 post-training quantization, pruning, layer fusion, and memory-mapped IO."
        }
    ],
    "NLP & LLM Engineer": [
        {
            "id": 1,
            "type": "Fine-Tuning & Quantization",
            "question": "Compare LoRA, QLoRA, and full fine-tuning. How does low-rank adaptation work mathematically, and what hyperparameters matter most?",
            "rubric": "Evaluates rank (r), alpha scaling, target modules (q_proj, v_proj), 4-bit NF4 quantization, and gradient checkpointing."
        }
    ],
    "Full-Stack AI Engineer": [
        {
            "id": 1,
            "type": "Full-Stack Streaming & State",
            "question": "How do you build a responsive, token-streaming AI chat interface with interactive citations that gracefully handles disconnections and rate limits?",
            "rubric": "Evaluates Server-Sent Events (SSE), WebSockets, client-side optimistic updates, backpressure handling, and reconnection recovery."
        }
    ],
    "AI Product & Analytics Specialist": [
        {
            "id": 1,
            "type": "AI Product Strategy & Metrics",
            "question": "How do you define success metrics and guardrail KPIs for an AI copilot feature before and after launching to production?",
            "rubric": "Evaluates task completion rate, user correction frequency, latency tolerance, hallucination rate, and customer ROI."
        }
    ]
}

class MockInterviewService:
    @staticmethod
    def get_interview_suite(role: str) -> List[Dict[str, Any]]:
        # Find exact or partial match for role
        for role_name, questions in ROLE_INTERVIEWS.items():
            if role.lower() in role_name.lower() or role_name.lower() in role.lower():
                return questions
        return ROLE_INTERVIEWS["Generative AI Engineer"]

    @staticmethod
    def evaluate_response(user_answer: str) -> Dict[str, Any]:
        words = user_answer.split()
        word_count = len(words)
        star_keywords = [
            "situation", "task", "action", "result", "metric", "improved", 
            "optimized", "bottleneck", "latency", "scaled", "trade-off", "architecture",
            "benchmark", "reduced", "qps", "throughput", "monitoring", "tested"
        ]
        hits = sum(1 for kw in star_keywords if kw in user_answer.lower())
        comm = min(96, max(45, 50 + int(word_count * 0.35)))
        tech = min(95, max(40, 52 + (hits * 5)))
        problem = min(94, max(45, 58 + (hits * 4)))
        overall = round((tech * 0.4 + comm * 0.3 + problem * 0.3), 1)
        feedback = []
        
        if word_count < 35:
            feedback.append("⚠️ Response is relatively brief. Provide deeper architectural trade-offs and specific tooling.")
        else:
            feedback.append("✅ Strong technical depth, clear structure, and substantial narrative detail.")
            
        if hits < 2:
            feedback.append("💡 Emphasize quantifiable metrics, specific numbers (latency, throughput), and STAR methodology.")
        else:
            feedback.append(f"✅ Excellent problem-solving structure highlighting concrete engineering impact ({hits} key technical indicators detected).")
            
        return {
            "overall_score": overall,
            "technical_score": tech,
            "communication_score": comm,
            "problem_solving_score": problem,
            "behavioral_score": 78.0,
            "feedback": feedback
        }
