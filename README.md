## Odmantic template

Odmantic template with **transaction support**

#### 1. Project structure:
````
odmantic_template/
├── examples/
│   ├── __init__.py
│   └── user_crud_service_example.py
├── scripts/
│   └── entrypoint.sh
├── src/
│   ├── common/
│   │   ├── dto/
│   │   │   ├── __init__.py
│   │   │   └── user.py
│   │   ├── interfaces/
│   │   │   ├── __init__.py
│   │   │   ├── repository.py
│   │   │   └── unit_of_work.py
│   │   ├── markers/
│   │   │   ├── __init__.py
│   │   │   └── gateway.py
│   │   ├── __init__.py
│   │   └── types.py
│   ├── core/  
│   │   ├── __init__.py
│   │   └── settings.py
│   ├── database/
│   │   ├── core/
│   │   │   ├── __init__.py
│   │   │   ├── connection.py
│   │   │   ├── gateway.py  
│   │   │   └── unit_of_work.py
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   └── user.py
│   │   ├── repositories/
│   │   │   ├── __init__.py
│   │   │   ├── odmantic_repository.py
│   │   │   └── user_repository.py
│   │   └── __init__.py
│   ├── __init__.py
│   └── __main__.py
├── .dockerignore
├── .env_example
├── .flake8
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── mypy.ini
├── README.md
└── requirements.txt
````

### 2. How to copy a project:
````
git clone https://github.com/mulphers/odmantic_template.git
````

### 3. Env-file:

Rename .env_example to .env and fill in

````
DATABASE_URI=mongodb://{}:{}
DATABASE_HOST=your_database_host
DATABASE_PORT=your_database_port
````

### 4. Run a project:

Go to your working directory and enter the command

````
docker-compose up
````

### 5. Database:

You can manage the database by following the link

Default login: admin

Default password: pass

````
http://127.0.0.1:8082
````
