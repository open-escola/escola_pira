### Alterações do DB

1. Deletar tudo da pasta `core/migrations`, com exceção do arquivo _**init**.py_
2. Rodar comando `python manage.py makemigrations`
3. Deletar tabelas do DB
4. Rodar comando `python manage.py migrate` para recriar

<br>

**É possível _resetar_ o DB do heroku!**

`heroku pg:reset DATABASE --app openescola`

<br>

---

