# Escola Pira

O projeto *Escola Pira* visa criar um sistema para auxiliar na gestão escolar. Possibilita cadastrar e editar os alunos
e professores, bem como classes e disciplinas.

O projeto foi desenvolvido com o *framework* Django.

-----

### Como acessar?!

[openescola.heroku.com](https://openescola.herokuapp.com/)

- login: admin@gmail.com
- senha: 111

-----

### Motivação

O presente projeto é resultado do trabalho do **Grupo 5** do *Projeto Integrador*, uma disciplina da UNIVESP, do Eixo da
Computação, Polo Piracicaba.

-----

### Template HTML

Foi utilizado o *template* [**AdminLTE**](https://adminlte.io/themes/v3/). É distribuído por meio da Licença MIT, que
possibilita uso.

Há um projeto que parece interessante e pode ser explorado, que é a adaptação desse template para
Django: [django-adminlte3](https://github.com/d-demirci/django-adminlte3) by [d-demirci](https://github.com/d-demirci)

-----

### Tutorial

Para realizar o trabalho, com adaptações para as necessidades para escolas brasileiras, bem como aperfeiçoamentos no
código, foi seguido o
tutorial [Python Django Student Management System ](https://www.youtube.com/watch?v=y3llbdTtam4&list=PLb-NlfexLTk_tUlAPj05s2zc8JgHTVkpH)
do canal [Super Coders](https://www.youtube.com/channel/UCyz5M_3Rv2jLUDs4R_yRBkw).

<br>

**Resumo**

1. *descrever*
2. *descrever*
3. *descrever*
4. *descrever*
5. *descrever*
6. *descrever*
7. *descrever*
8. *descrever*
9. *descrever*
10. *descrever*
11. Funções em AJAX para Attendance no perfil Staff!

*(Em 03.10.2021 concluí parte 11)*

<br>

**Outros**

Há ainda outros canais com sistemas similares para gestão educacional.

**Programming with Singhateh**

- https://www.youtube.com/watch?v=1A4tyUQTizM
- https://www.youtube.com/watch?v=TYrXsAGNVrY

-----

### Quem Somos

*Em ordem alfabética*

- Ana Paula
- Ana Gabrielle
- [João Victor](https://github.com/JvPelai)
- Joseana
- Kevin
- Marcel Alessandro
- [Michel Metran](https://github.com/michelmetran)
- Michele

----

### Como usar?

#### Na Máquina Local

Para testes, customizações etc.

1) Criar um banco de dados conforme especificações contidas em *settings.py*.
 (Opcional: ```docker-compose up```, é necessário ter o [docker](https://www.docker.com/get-started/) instalado localmente).
2) Instalar as dependências do projeto ```pip install -r requirements.txt```.
3) Rodar o comando ```python manage.py makemigrations``` para criar as querys que criarão as tabelas.
4) Rodar o comando ```python manage.py migrate``` para alterar o banco de dados.
5) Rodar o comando ```python manage.py runserver``` para iniciar o servidor *gunicorn*.

#### Em um site

Explicar como fazer *deploy* no Heroku ou *Docker*

----


### *ToDo*

- Corrigir *migrations* do *background-image: url("images/ui-icons_555555_256x240.png");*
- Ajustar *dump* e *load*

----

### Alterações do DB

1. Deletar tudo da pasta ```core/migrations```, com exceção do arquivo *__init__.py*
2. Rodar comando ```python manage.py makemigrations```
3. Deletar tabelas do DB
4. Rodar comando ```python manage.py migrate``` para recriar

<br>

**É possível *resetar* o DB do heroku!**

```heroku pg:reset DATABASE --app openescola```

----

### Dados de Exemplo

```
# Load Local
python manage.py loaddata admin.json
python manage.py loaddata initial_data.json
python manage.py loaddata students.json

# Load Server
heroku run python manage.py loaddata admin.json --app openescola
heroku run python manage.py loaddata initial_data.json --app openescola
heroku run python manage.py loaddata students.json --app openescola
```


