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
Middleware(log_requests)
  |
Register(register_models)
  |
FastAPI Router
  |
Depends(query_service)
  |
QueryService
  |
Provider  [lru_cache]
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

## 2 Run API

uvicorn application.entry.app:app --reload

## 3 Test API

POST

http://localhost:8000/docs

Example payload:
{
"name":"AI Platform",
"query":"What is AI agent?"
}
