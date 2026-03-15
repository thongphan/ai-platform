# Desired Architecture

Features included:
- Kafka Event Streaming
- Temporal-style Workflow Orchestration (local simulator)
- LLM Planning Agents (stub)
- Vector Memory Retrieval
- Graph Knowledge Reasoning
- Multi-Agent Negotiation
- AI CTO Architecture
- Kubernetes Autoscaling Worker Simulation
# Data and system Architecture

FastAPI API
     ↓
Kafka topic: project_events
     ↓
Agent Worker
     ↓
PlanningAgent.run()
     ↓
Temporal.start_workflow()
     ↓
Temporal Workflow Engine
     ↓
Temporal Worker executes tasks


Run locally.

## 1 Install

pip install -r requirements.txt

## 2 Start Kafka

docker-compose up -d

## 3 Run API

uvicorn app:app --reload

## 4 Run Worker

python workers/agent_worker.py

## 5 Test API

POST

http://localhost:8000/query

Example payload:

{
"name":"AI Platform",
"query":"What is AI agent?"
}
