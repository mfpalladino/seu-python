# 🐍 Seu Python - Assistente Virtual Python Brasil 2025

> Um chatbot inteligente e bem-humorado para a conferência Python Brasil 2025, desenvolvido com Amazon Bedrock Knowledge Base e RAG.

## 🎯 Sobre o Projeto

O **Seu Python** é um assistente virtual especializado que atua como guia para os participantes da Python Brasil 2025. Com personalidade pythonista e conhecimento técnico profundo, ele ajuda os participantes a navegar pela programação do evento, descobrir atividades relevantes e aproveitar ao máximo a conferência.

### 🚀 Nascido no AWS Vibe Coding Dojo

Este projeto foi criado com muito **Python hacking love** 💚 durante o **AWS Vibe Coding Dojo** na Python Brasil 2025! 

Em uma sessão de programação colaborativa utilizando o Amazon Q Developer, onde desenvolvedores se reuniram para hackear soluções inovadoras usando IA e AWS, o Seu Python ganhou vida. Entre `import antigravity`, risadas sobre indentação e muito café ☕, transformamos uma ideia maluca em realidade usando o poder do Amazon Bedrock.

**O resultado?** Um bot que não só conhece Python como ninguém, mas também tem o humor característico da nossa comunidade pythonista brasileira! 🇧🇷🐍

*"Porque todo bom código Python precisa de uma boa dose de diversão e colaboração!"*

### Características Principais

- 🧠 **IA Conversacional**: Powered by Amazon Bedrock com Knowledge Base RAG
- 🎭 **Personalidade Pythonista**: Humor característico da comunidade Python
- 📚 **Base de Conhecimento**: Informações sobre palestras, workshops e keynotes da Python Brasil 2025
- 🎨 **Interface Moderna**: Frontend React + Vite responsivo

### Stack Tecnológica

**Frontend:**
- React 18
- Vite
- CSS moderno

**Backend:**
- FastAPI
- Boto3 (AWS SDK)
- Python 3.11+

**IA & Dados:**
- Amazon Bedrock Knowledge Base
- Amazon Nova Micro (LLM)
- Titan Embedding V2 (Embeddings)
- RAG Pattern (Retrieval-Augmented Generation)

## 🚀 Início Rápido

### Pré-requisitos

- Python 3.11+
- Node.js 18+
- AWS CLI configurado
- Credenciais AWS com acesso ao Bedrock

### Instalação

1. **Clone o repositório:**
```bash
git clone <repository-url>
cd seu-python
```

2. **Configure o backend:**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

3. **Configure o frontend:**
```bash
cd ../frontend
npm install
```

4. **Configure as variáveis de ambiente:**
```bash
# backend/.env
AWS_REGION=us-east-1
BEDROCK_KNOWLEDGE_BASE_ID=your-kb-id
BEDROCK_MODEL_ID=your-model-id
```

### Executando o Projeto

1. **Inicie o backend:**
```bash
cd backend
source venv/bin/activate
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

2. **Inicie o frontend:**
```bash
cd frontend
npm run dev
```

3. **Acesse a aplicação:**
- Frontend: http://localhost:5173
- Backend API: http://localhost:8000
- Documentação API: http://localhost:8000/docs

## 🤖 Funcionalidades

### Core Features

- **Navegação na Programação**: Busca por palestras, workshops e keynotes
- **Recomendações Personalizadas**: Sugestões baseadas em interesses
- **Informações do Evento**: Detalhes sobre localização e logística
- **Assistência Contextual**: Respostas baseadas na base de conhecimento

### Personalidade do Bot

O Seu Python incorpora:
- 🎭 Referências ao Monty Python
- 🐍 Piadas sobre indentação e PEP 8
- 🚀 Trocadilhos com "snake" e "python"
- 🥚 Easter eggs da linguagem Python
- 🇧🇷 Humor brasileiro adaptado à comunidade tech

## 🛠️ Desenvolvimento

### Comandos Úteis

```bash
# Backend
cd backend
source venv/bin/activate
uvicorn app.main:app --reload    # Desenvolvimento
python -m pytest                # Testes

# Frontend  
cd frontend
npm run dev                      # Desenvolvimento
npm run build                    # Build produção
npm run preview                  # Preview build
```

### Estrutura da API

```
GET  /                          # Health check
POST /chat                      # Endpoint principal do chat
GET  /docs                      # Documentação Swagger
```

### Exemplo de Uso da API

```bash
curl -X POST "http://localhost:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{"message": "Quais são as palestras sobre FastAPI?"}'
```

## 🔧 Configuração AWS

### Bedrock Knowledge Base

1. **Crie um Knowledge Base no Amazon Bedrock**
2. **Configure o data source** com os arquivos da pasta `knowledge-base/`
3. **Execute a sincronização** dos documentos
4. **Anote o Knowledge Base ID** para as variáveis de ambiente

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para detalhes.

---

<div align="center">

**Feito com ❤️ para a comunidade Python Brasil 2025**

🐍 *"import antigravity"* 🚀

</div>
