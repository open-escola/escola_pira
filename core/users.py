"""
Preciso fazer um script que adicione usuários!
Os SuperUsuários conseguem acessar o sistema
python manage.py createsuperuser --email michelmetran@gmail.com --username michelmetran
"""

from core.models import CustomUser

user = CustomUser.objects.create_user(
    username='sseber',
    password='12345',
    email='sseber@gmail.com',
    first_name='Samile',
    last_name='Seber',
    user_type=1,
)

user.save()


