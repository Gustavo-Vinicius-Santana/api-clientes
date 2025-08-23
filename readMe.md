# Projeto Flask - Estrutura Organizada

Este projeto é um template Flask com arquitetura organizada:

- `app/routes/` → rotas da aplicação (BluePrints)
- `app/services/` → lógica de negócio
- `app/repositories/` → acesso ao banco
- `app/models/` → modelos SQLAlchemy
- `app/extensions.py` → inicialização de extensões (SQLAlchemy, Migrate)
- `app/config.py` → configuração da aplicação
- `run.py` → ponto de entrada da aplicação
- Banco de dados padrão: **SQLite**

---

## 1. Pré-requisitos

- Python 3.10 ou superior
- `pip` instalado
- (Opcional) Editor de código: VSCode, PyCharm, etc.

---

## 2. Criar e ativar o ambiente virtual

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar (Windows CMD)
venv\Scripts\activate

# Ativar (PowerShell)
$env:VIRTUAL_ENV="venv"
venv\Scripts\activate

# Ativar (Linux / Mac)
source venv/bin/activate

```

## 3. Criar e ativar o ambiente virtual

```bash
pip install -r requirements.txt
```
Se não tiver requirements.txt, instale manualmente:

```bash
pip install flask flask_sqlalchemy flask_migrate
```

## 4. Configurar variável de ambiente Flask

- windows CMD:

```bash
set FLASK_APP=app:create_app
```

- windows powerShell:
```bash
$env:FLASK_APP="app:create_app"
```

- linux / mac:

```bash
export FLASK_APP=app:create_app
```

## 5. Inicializar o banco de dados (SQLite) com Flask-Migrate

```bash
# Inicializa a pasta de migrations
flask db init

# Cria a primeira migration baseada nos models
flask db migrate -m "Initial migration"

# Aplica as migrations no banco
flask db upgrade
```

o arquivo db.sliqte será criado na raiz do projeto.

## 6. Rodar a aplicação

```bash
python run.py
```

Acesse no navegador:
- http://127.0.0.1:5000/ → retorna JSON {"mensagem": "Hello, Flask!", "status": "sucesso"}
- http://127.0.0.1:5000/sobre → retorna JSON {"mensagem": "Sobre a aplicação"}

## 7. Estrutura de pastas

```arduino
api-clientes/
│── app/
│   │── __init__.py
│   │── config.py
│   │── extensions.py
│   │── routes/
│   │    └── main_routes.py
│   │── services/
│   │── repositories/
│   │── models/
│
│── run.py
│── requirements.txt
│── db.sqlite  (após upgrade)
│── .gitignore
```

## 8. Observações

- Para desenvolvimento, você pode manter debug=True em run.py.
- O banco padrão é SQLite, mas pode ser substituído por PostgreSQL, MySQL ou outro alterando SQLALCHEMY_DATABASE_URI em app/config.py.
- Blueprints e arquitetura modular permitem adicionar novas rotas, serviços e repositórios facilmente.


