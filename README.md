# 🦖 PaleoDex API

API REST desenvolvida com **FastAPI** para gerenciar fósseis de dinossauros.  
Permite cadastrar **espécimes**, **museus** e **taxons**, utilizando **SQLAlchemy assíncrono** e validação de dados com **Pydantic**.

[![Python](https://img.shields.io/badge/python-3.11%2B-blue.svg?logo=python)](https://www.python.org/downloads/release/python-3110/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688.svg?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Postgres](https://img.shields.io/badge/Postgres-11+-336791.svg?logo=postgresql)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker-ready-2496ED.svg?logo=docker)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Made with Love](https://img.shields.io/badge/Made%20with-❤️-white.svg)](#)

---

## 📁 Estrutura do Projeto
```
paleodex_api/
├── configs/
│   ├── database.py      # Conexão assíncrona com o Postgres
│   └── settings.py      # Variáveis de ambiente (URL do banco)
├── contrib/
│   ├── models.py        # BaseModel com UUID para todas as tabelas
│   └── schemas.py       # BaseSchema com configuração comum aos DTOs
├── especime/            # Recursos relacionados aos fósseis
├── museu/               # Recursos de museus
├── taxons/              # Recursos de taxonomia
├── routers.py           # Registra os módulos de rotas
└── main.py              # Inicializa a aplicação FastAPI
```
📌 Migrations do banco ficam em alembic/  
📌 O container do Postgres é definido em docker-compose.yml.

--- 

## 🚀 Pré-requisitos

- Python 3.11+
- Docker (opcional, para Postgres local)
- Postgres 11+ (caso não use Docker)

--- 

## 🛠️ Instalação

```
git clone https://github.com/seu_usuario/PaleoDex_API.git
cd PaleoDex_API
```
```
python -m venv .venv
venv\Scripts\activate      # Windows PowerShell
```
```
pip install -r requirements.txt
```

--- 

## 🗄️ Banco de Dados

```docker-compose up -d```

```DB_URL=postgresql+asyncpg://PaleoDex:PaleoDex@localhost/PaleoDex```

--- 

## 📚 Migrações
```
make create-migrations d="mensagem_da_migration"
make run-migrations
```

--- 

## ▶️ Execução
```
make run
uvicorn paleodex_api.main:app --reload
```
Swagger: http://localhost:8000/docs  
Redoc:   http://localhost:8000/redoc  

--- 

## 🧪 Endpoints

- /especimes  
- /museus  
- /taxons  

--- 

## 🤝 Contribuição

1. Abra uma issue ou discuta a ideia  
2. Faça um fork  
3. Crie uma branch  
4. Envie um PR  

--- 

## 📄 Licença

Ainda não há licença definida.  

💡 Bom desenvolvimento! 🦕
