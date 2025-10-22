# Base de Conhecimento - Python Brasil 2025

Esta pasta contém todos os dados estruturados sobre a Python Brasil 2025 que serão utilizados pelo sistema RAG (Retrieval-Augmented Generation) do chatbot "Seu Python".

## Estrutura

- `palestras/` - Informações sobre todas as palestras do evento
- `workshops/` - Detalhes dos workshops e tutoriais
- `keynotes/` - Palestras principais e keynotes
- `patrocinadores/` - Informações sobre patrocinadores e expositores
- `informacoes-gerais/` - Dados gerais do evento (local, horários, etc.)

## Formato dos Arquivos

Cada arquivo deve conter informações estruturadas em markdown para facilitar a indexação pelo Bedrock Knowledge Base.

### Template para Palestras:
```markdown
# [Título da Palestra]

**Palestrante:** [Nome]
**Horário:** [Data e hora]
**Local:** [Sala/Auditório]
**Duração:** [Tempo]
**Nível:** [Iniciante/Intermediário/Avançado]

## Resumo
[Descrição da palestra]

## Sobre o Palestrante
[Bio do palestrante]

## Tags
[python, web, data-science, etc.]
```

## Instruções

1. Extraia as informações do site https://talks.python.org.br/pythonbrasil-2025/schedule/
2. Crie um arquivo .md para cada palestra/workshop
3. Use nomes de arquivo descritivos (ex: `machine-learning-python-joao-silva.md`)
4. Mantenha consistência no formato para melhor indexação
