# Escola Pira


O projeto *Escola Pira* visa criar um sistema para auxiliar na gestão escolar. Possibilita cadastrar e editar os alunos
e professores, bem como classes e disciplinas.

(Teste)

O projeto foi desenvolvido com o *framework* Django.

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

Há ainda outros canais com sistemas similares para gestão educacional.

**Programming with Singhateh**

- https://www.youtube.com/watch?v=1A4tyUQTizM
- https://www.youtube.com/watch?v=TYrXsAGNVrY

*(Em 09.09.2021 parei nos 20 minutos da parte 11)*

-----


### Quem Somos

- Ana Paula
- Ana Gabrielle
- Joseana
- Kevin
- [Michel Metran](https://github.com/michelmetran)
- Michele

----


### Como usar?


#### Na Máquina Local


Para testes, customizações etc.

1. Criar um banco de dados conforme especificações contidas em *settings.py*;
2. Rodar o comando ```python manage.py makemigrations``` para criar as querys que criarão as tabelas;
3. Rodar o comando ```python manage.py migrate``` para alterar o banco de dados.
4. Rodar o comando ```python manage.py runserver``` para iniciar o servidor *gunicorn*.

#### Em um site


Explicar como fazer *deploy* no Heroku ou *Docker*

----


### Dados de Exemplo

```
python manage.py loaddata subjects.json
python manage.py loaddata courses.json
python manage.py createsuperuser --email admin@example.com --username admin
```

----


### TODO

- Corrigir *migrations* do *background-image: url("images/ui-icons_555555_256x240.png");*
- ...
- 



