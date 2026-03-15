# Desired architecture
To scale an enterprise AI platform
API Layer
   |
Application Layer
   |
AI Orchestration Layer
   |
Model Provider Layer
   |
Infrastructure Layer

# End-to-End Flow Architecture
Request lifecycle in your current design
Client
  |
FastAPI Router
  |
Depends(Container.query_service)
  |
QueryService
  |
LLMModel abstraction
  |
ModelFactory
  |
Concrete Model (OllamaModel / OpenAIModel)
  |
LLM API
Expanded dependency resolution
FastAPI Request
    |
    v
APIRouter /ai/query
    |
    v
Container.query_service()  [lru_cache]
    |
    +---- Container.model() [lru_cache]
              |
              +---- SettingsProvider.get_settings()
              |          |
              |          +---- ConfigLoader.load(config.yaml)
              |
              +---- ModelFactory.create(settings)
                          |
                          +---- OllamaModel(...)
                          +---- OpenAIModel(...)

Run locally.

## 1 Install

pip install -r requirements.txt

## 2 Start Kafka

docker-compose up -d

## 3 Run API

uvicorn application.entry.app:app --reload

## 4 Test API

POST

http://localhost:8000/query

Example payload:

{
"name":"AI Platform",
"query":"What is AI agent?"
}
