from typing import List, Dict

class RoadmapService:
    CURRICULUM_MAP = {
        "RAG": "Vector DBs (Chroma/Qdrant/Pinecone), Semantic Chunking, Hybrid Search (BM25 + Dense), Cross-Encoder Rerankers & Ragas evaluation.",
        "AI Agents": "LangGraph state graphs, Tool calling protocols, Multi-agent supervisor patterns, Memory retention & Cyclic flows.",
        "System Design": "Low-latency streaming architectures, Caching strategies (Redis), Asynchronous workers, Quantization, Rate limiters.",
        "Deep Learning": "Transformers architecture, Multi-Head Attention, Backpropagation mechanics, Loss functions, GPU optimization.",
        "LLMs": "Prompt engineering patterns, Structured JSON extraction with Pydantic, DSPy optimization, Guardrails, Context window optimization.",
        "PyTorch": "Custom Dataset/DataLoader pipelines, Tensor manipulations, TorchScript/ONNX export, Multi-GPU DistributedDataParallel training.",
        "Machine Learning": "Feature engineering, Regularization (L1/L2), Ensemble methods (XGBoost/LightGBM), Cross-validation, Hyperparameter optimization with Optuna.",
        "MLOps": "CI/CD for ML, MLflow model registry, Kubeflow pipelines, Dockerized inference services, Prometheus metric exporters.",
        "Spark": "PySpark DataFrames, Spark Structured Streaming, Watermarking, Catalyst Optimizer, Partitioning & Shuffle optimization.",
        "Kafka": "Topic partitioning, Consumer groups, Offset management, Avro Schema Registry, Event-driven microservices.",
        "Airflow": "Dynamic DAG authoring, Custom Operators, Sensor tasks, XCom data passing, Task retries & SLA monitoring.",
        "PostgreSQL": "Indexing strategies (B-Tree, GIN, BRIN), Window functions, CTEs, Query execution plans (EXPLAIN ANALYZE), ACID transactions.",
        "Docker": "Multi-stage builds, Distroless images, Container networking, Volume mounts, Docker Compose orchestration.",
        "Kubernetes": "Deployments, Services, Ingress controllers, Horizontal Pod Autoscaling (HPA), Resource requests & limits, Helm charts.",
        "OpenCV": "Image transformations, Edge detection, Color spaces, Video stream decoding, GStreamer pipelines, Contour analysis.",
        "Object Detection": "YOLO architectures, Region Proposal Networks (Faster R-CNN), Non-Maximum Suppression (NMS), mAP calculation, Dataset augmentation.",
        "Fine-Tuning / LoRA": "Parameter-Efficient Fine-Tuning (PEFT), LoRA/QLoRA mathematical intuition, 4-bit quantization (bitsandbytes), Instruction tuning.",
        "React / Next.js": "App Router, Server-Sent Events (SSE) streaming, Client vs Server components, Zustand state management, Tailwind CSS.",
        "Statistics & Probability": "Hypothesis testing, P-values, Confidence intervals, Bayesian inference, Sampling distributions, Regression diagnostics.",
        "A/B Testing": "Sample size calculation, Statistical power, Minimum Detectable Effect (MDE), Network effects, Sequential testing."
    }

    @staticmethod
    def generate_personalized_roadmap(top_gaps: List[Dict]) -> List[Dict]:
        roadmap = []
        week = 1
        for item in top_gaps:
            if item.get("gap", 0) > 0:
                skill = item["skill"]
                focus = RoadmapService.CURRICULUM_MAP.get(
                    skill, 
                    f"Core principles, hands-on production implementations, system trade-offs, and practical project application for {skill}."
                )
                roadmap.append({
                    "timeframe": f"Weeks {week} - {week + 1}",
                    "skill": skill,
                    "gap": item["gap"],
                    "priority_score": item.get("priority_score", item["gap"] * 3),
                    "focus": focus
                })
                week += 2
                
        if not roadmap:
            roadmap.append({
                "timeframe": "Ongoing",
                "skill": "Advanced Production Engineering & Architecture",
                "gap": 0,
                "priority_score": 0,
                "focus": "High-throughput low-latency serving, Open-source contributions, distributed fault tolerance, and System Design."
            })
        return roadmap
