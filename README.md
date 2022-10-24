# Escola Pira


<br>

O projeto _Escola Pira_ visa criar um sistema para auxiliar na gestão escolar. Possibilita cadastrar e editar os alunos
e professores, bem como classes e disciplinas.

O projeto foi desenvolvido com o _framework_ Django.

Para mais informações ver [Wiki](https://github.com/open-escola/escola_pira/wiki)

<br>

---


### ENV


C

```bash
conda create --name webapp-py310 -c conda-forge python=3.10 django django-heroku dj-database-url gunicorn pytz requests django-heroku whitenoise cryptography psycopg2 PyYAML
```

### _TODO_

1. Corrigir _migrations_ do _background-image: url("images/ui-icons_555555_256x240.png");_
2. ~~(Ok) Ajustar _dump_ e _load_~~
3. ~~(Ok) Ajustar _load data_, devido a alterações no endereço (04.2022)~~
