#### Na Máquina Local


Para testes, customizações etc.

<br>


Estou usando o gerenciador de pacotes conda para desenvolvimento do projeto.
Logo, a primeira etapa foi criar um *enviroment* com todas as dependências.

```bash
conda create --name webapp-py310 -c conda-forge python=3.10 django==4.1 django-heroku dj-database-url gunicorn pytz requests django-heroku whitenoise cryptography psycopg2 PyYAML numpy pandas djangorestframework
```

<br>

1. Criar um banco de dados conforme especificações contidas em _settings.py_.<br>

> **_Opcional_**<br>
> Visando não precisar instalar o banco de dados PostGre localmente, é possível instancia-lo usando docker.
> Para isso é necessário ter o [docker](https://www.docker.com/get-started/)
> e [docker-compose](https://docs.docker.com/compose/compose-file/) instalado.<br>
> Após isso basta rodar o comando `docker-compose up -d`

2. Instalar as dependências do projeto `pip install -r requirements.txt`.
3. Rodar o comando `python manage.py makemigrations` para criar as _querys_ que criarão as tabelas.
4. Rodar o comando `python manage.py migrate` para alterar o banco de dados.
5. Rodar o comando `python manage.py runserver` para iniciar o servidor _gunicorn_.
6. Para adicionar dados:

```bash
# Load Local
python manage.py loaddata admin.json
python manage.py loaddata initial_data.json
python manage.py loaddata students.json
```

<br>

----


#### Em um site


Explicar como fazer _deploy_ no Heroku ou _Docker_

1. Criar copia do repositorio
2. Vincular a sua conta Heroku
3. Para adicionar dados:

```bash
# Load Server
heroku run python manage.py loaddata admin.json --app openescola
heroku run python manage.py loaddata initial_data.json --app openescola
heroku run python manage.py loaddata students.json --app openescola
```

