import boto3
from .config import settings

class BedrockService:
    def __init__(self):
        self.bedrock_agent_runtime = boto3.client(
            'bedrock-agent-runtime',
            region_name=settings.aws_region
        )
        
    async def get_response(self, user_message: str) -> str:
        try:
            # Usar Knowledge Base para RAG
            response = self.bedrock_agent_runtime.retrieve_and_generate(
                input={
                    'text': user_message
                },
                retrieveAndGenerateConfiguration={
                    'type': 'KNOWLEDGE_BASE',
                    'knowledgeBaseConfiguration': {
                        'knowledgeBaseId': settings.bedrock_knowledge_base_id,
                        'modelArn': settings.bedrock_model_id,
                        'generationConfiguration': {
                            'promptTemplate': {
                                'textPromptTemplate': '''Você é o Seu Python, um assistente especialista em Python criado para a Python Brasil 2025.

Características da sua personalidade:
- Especialista Python experiente e bem-humorado
- Usa referências do Monty Python e da comunidade Python
- Faz piadas sobre indentação, PEP 8, e "import antigravity"
- Linguagem acessível mas tecnicamente precisa
- Entusiasmado com a comunidade Python brasileira

Use as informações fornecidas sobre a Python Brasil 2025 para responder à pergunta do usuário de forma útil, divertida e pythônica.

Pergunta: $query$

Informações relevantes: $search_results$

Resposta:'''
                            }
                        }
                    }
                }
            )
            
            return response['output']['text']
            
        except Exception as e:
            return f"Ops! Algo deu errado no meu cérebro pythônico: {str(e)}"
