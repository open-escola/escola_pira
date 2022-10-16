### Como usar?


#### Na Máquina Local


Para testes, customizações etc.

1. Criar um banco de dados conforme especificações contidas em _settings.py_.<br>
   _Opcional_: `docker-compose up`, é necessário ter o [docker](https://www.docker.com/get-started/) instalado
   localmente).
2. Instalar as dependências do projeto `pip install -r requirements.txt`.
3. Rodar o comando `python manage.py makemigrations` para criar as querys que criarão as tabelas.
4. Rodar o comando `python manage.py migrate` para alterar o banco de dados.
5. Rodar o comando `python manage.py runserver` para iniciar o servidor _gunicorn_.
6. Para executar testes unitários: `python manage.py test core/test`.
7. Para adicionar dados:

```bash
# Load Local
python manage.py loaddata admin.json
python manage.py loaddata initial_data.json
python manage.py loaddata students.json
```

<br>


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

