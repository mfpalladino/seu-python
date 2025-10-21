# Arquitetura Técnica - Seu Python

## Componentes da Arquitetura

### Frontend
- **React + Vite**: Interface de chat responsiva
- **WebSocket/HTTP**: Comunicação com backend

### Backend
- **FastAPI**: API REST para processamento de mensagens
- **Boto3**: SDK AWS para integração com Bedrock

### IA e Dados
- **Amazon Bedrock**: LLM para geração de respostas
- **Bedrock Knowledge Base**: RAG com dados da conferência Python Brasil 2025

## Fluxo de Dados

```
[React Chat] → [FastAPI] → [Bedrock KB] → [LLM] → [Resposta]
```

## Decisões Arquiteturais

1. **Stateless**: Sem sessão persistente, contexto via Knowledge Base
2. **RAG Pattern**: Recuperação de informações + geração de resposta
3. **Serverless Ready**: FastAPI compatível com Lambda para produção
4. **Local First**: Desenvolvimento 100% local com AWS remoto
