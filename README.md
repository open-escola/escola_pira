# Escola Pira


O projeto *Escola Pira* visa criar um sistema para auxiliar na gestão escolar. Possibilita cadastrar e editar os alunos
e professores, bem como classes e disciplinas.

O projeto foi desenvolvido com o *framework* Django.

<br>

-----


### Como acessar?!


[openescola.heroku.com](https://openescola.herokuapp.com/)

- login: admin@gmail.com
- senha: 111

<br>

-----


### Motivação


O presente projeto é resultado do trabalho do **Grupo 5** do *Projeto Integrador*, uma disciplina da UNIVESP, do Eixo da
Computação, Polo Piracicaba.

<br>

-----


### Quem Somos


*Em ordem alfabética*

- Ana Paula
- Felipe Assalin
- Gabrielle Lombardi
- Isabelle Zein
- [João Victor](https://github.com/JvPelai)
- Marcel Alessandro
- [Michel Metran](https://github.com/michelmetran)
- Michele Pertille

<br>

-----


### Tutorial


Para realizar o trabalho, com adaptações para as necessidades para escolas brasileiras, bem como aperfeiçoamentos no
código, foi seguido o
tutorial [Python Django Student Management System](https://www.youtube.com/watch?v=y3llbdTtam4&list=PLb-NlfexLTk_tUlAPj05s2zc8JgHTVkpH)
do canal [Super Coders](https://www.youtube.com/channel/UCyz5M_3Rv2jLUDs4R_yRBkw).

Há ainda outros canais com sistemas similares para gestão educacional, por exemplo a
playlist [How to create python django School Management System](https://www.youtube.com/watch?v=a5dlmqM9Oo8&list=PLIeKz8l1eVaNu3pcciZRmyRf9oj3F4X6i)
do canal [Programming with Singhateh](https://www.youtube.com/c/SinghatehAlagie)

<br>

**Resumo**

11. Funções em AJAX para Attendance no perfil Staff!

*Em 03.10.2021 concluí parte 11*
*Durante o primeiro semestre de 2022 fiz varias modificaçoes sem seguir tutorial*

<br>

**Template HTML**

Foi utilizado o *template* [**AdminLTE**](https://adminlte.io/themes/v3/). É distribuído por meio da Licença MIT, que
possibilita uso.

Há um projeto que parece interessante e pode ser explorado, que é a adaptação desse template para
Django: [django-adminlte3](https://github.com/d-demirci/django-adminlte3) by [d-demirci](https://github.com/d-demirci)

----


### Como usar?


#### Na Máquina Local


Para testes, customizações etc.

1. Criar um banco de dados conforme especificações contidas em *settings.py*.<br>
   *Opcional*: ```docker-compose up```, é necessário ter o [docker](https://www.docker.com/get-started/) instalado
   localmente).
2. Instalar as dependências do projeto ```pip install -r requirements.txt```.
3. Rodar o comando ```python manage.py makemigrations``` para criar as querys que criarão as tabelas.
4. Rodar o comando ```python manage.py migrate``` para alterar o banco de dados.
5. Rodar o comando ```python manage.py runserver``` para iniciar o servidor *gunicorn*.
6. Para executar testes unitários: ```python manage.py test core/test```.

#### Em um site


Explicar como fazer *deploy* no Heroku ou *Docker*

1. Criar copia do repositorio
2. Vincular a sua conta Heroku

<br>

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

```bash
# Load Local
python manage.py loaddata admin.json
python manage.py loaddata initial_data.json
python manage.py loaddata students.json

# Load Server
heroku run python manage.py loaddata admin.json --app openescola
heroku run python manage.py loaddata initial_data.json --app openescola
heroku run python manage.py loaddata students.json --app openescola
```

<br>

-----


### API

- [CEPs Automáticos](https://velhobit.com.br/programacao/carregando-cep-cidades-dinamicamente.html)
- [Como consumir uma API no Frontend](https://www.youtube.com/watch?v=UDoCiC_e908)

<br>

----


### SuperUser

```
python manage.py createsuperuser --email admin@gmail.com --username admin --app openescola
heroku run python manage.py createsuperuser --email admin@gmail.com --username admin --app openescola
```

<br>

----


### *TODO*

1. Corrigir *migrations* do *background-image: url("images/ui-icons_555555_256x240.png");*
2. (Ok) Ajustar *dump* e *load*
3. (Ok) Ajustar *load data*, devido a alterações no endereço (04.2022)
