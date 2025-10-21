# 🐍 Seu Python - Assistente Virtual Python Brasil 2025

> Um chatbot inteligente e bem-humorado para a conferência Python Brasil 2025, desenvolvido com Amazon Bedrock Knowledge Base e RAG.

## 🎯 Sobre o Projeto

O **Seu Python** é um assistente virtual especializado que atua como guia para os participantes da Python Brasil 2025. Com personalidade pythonista e conhecimento técnico profundo, ele ajuda os participantes a navegar pela programação do evento, descobrir atividades relevantes e aproveitar ao máximo a conferência.

### Características Principais

- 🧠 **IA Conversacional**: Powered by Amazon Bedrock com Knowledge Base RAG
- 🎭 **Personalidade Pythonista**: Humor característico da comunidade Python
- 📚 **Base de Conhecimento**: Informações completas sobre palestras, workshops e keynotes
- ⚡ **Respostas Rápidas**: Arquitetura otimizada para baixa latência
- 🎨 **Interface Moderna**: Frontend React + Vite responsivo

## 🏗️ Arquitetura

```
┌─────────────────┐    ┌──────────────┐    ┌─────────────────────┐
│   React + Vite  │───▶│   FastAPI    │───▶│  Amazon Bedrock KB  │
│   (Frontend)    │    │  (Backend)   │    │       (RAG)         │
└─────────────────┘    └──────────────┘    └─────────────────────┘
                                                      │
                                                      ▼
                                            ┌─────────────────────┐
                                            │    Nova Micro LLM   │
                                            │   (Geração de       │
                                            │    Respostas)       │
                                            └─────────────────────┘
```

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
BEDROCK_MODEL_ID=amazon.nova-micro-v1:0
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

## 📁 Estrutura do Projeto

```
seu-python/
├── 📁 backend/                 # API FastAPI
│   ├── 📁 app/
│   │   ├── main.py            # Aplicação principal
│   │   ├── bedrock_service.py # Serviço Bedrock
│   │   └── config.py          # Configurações
│   ├── requirements.txt       # Dependências Python
│   └── 📁 venv/              # Ambiente virtual
├── 📁 frontend/               # Interface React
│   ├── 📁 src/
│   │   ├── App.jsx           # Componente principal
│   │   ├── App.css           # Estilos
│   │   └── main.jsx          # Entry point
│   ├── package.json          # Dependências Node
│   └── vite.config.js        # Configuração Vite
├── 📁 knowledge-base/         # Base de conhecimento
│   ├── 📁 palestras/         # Informações das palestras
│   ├── 📁 workshops/         # Detalhes dos workshops
│   ├── 📁 keynotes/          # Keynotes principais
│   ├── 📁 informacoes-gerais/# Info geral do evento
│   └── 📁 patrocinadores/    # Dados dos patrocinadores
├── 📁 docs/                   # Documentação
│   ├── definicao-produto.md  # Especificação do produto
│   └── arquitetura-tecnica.md# Arquitetura técnica
└── README.md                  # Este arquivo
```

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

### Modelos Necessários

- **Nova Micro**: Para geração de respostas (custo-efetivo)
- **Titan Embedding V2**: Para embeddings dos documentos

## 💰 Estimativa de Custos

Para 5.000 interações durante o evento:

| Componente | Custo Estimado |
|------------|----------------|
| Knowledge Base Retrieval | $30.00 |
| Nova Micro (Input/Output) | $0.17 |
| Titan Embeddings | $0.02 |
| **Total** | **~$30.19** |

> Custos baseados em preços ON DEMAND da região us-east-1

## 🚀 Deploy

### Opções de Deploy

1. **Local Development**: FastAPI + React dev servers
2. **AWS Lambda**: Serverless backend com API Gateway
3. **EC2/ECS**: Containerized deployment
4. **Amplify**: Frontend hosting

### Deploy Serverless (Recomendado)

```bash
# Instalar dependências de deploy
pip install mangum

# Configurar Lambda handler
# Ver documentação específica em docs/
```

## 🤝 Contribuindo

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👥 Equipe

- **Desenvolvimento**: Equipe Python Brasil 2025
- **IA/ML**: Amazon Bedrock Integration
- **Frontend**: React + Vite Stack

## 📞 Suporte

- 📧 Email: contato@pythonbrasil.org.br
- 🐛 Issues: [GitHub Issues](../../issues)
- 💬 Discussões: [GitHub Discussions](../../discussions)

---

<div align="center">

**Feito com ❤️ para a comunidade Python Brasil 2025**

🐍 *"import antigravity"* 🚀

</div>
