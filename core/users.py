from django.contrib.auth.models import User

from core.models import CustomUser

# u = CustomUser(username='unique_fellow')
# u.set_password('12345')
# u.is_superuser = True
# u.is_staff = True
# u.is_active = True
# u.user_type = 1
# u.save()

user = CustomUser.objects.create_user(
    username='sseber',
    password='12345',
    email='sseber@gmail.com',
    first_name='Samile',
    last_name='Seber',
    user_type=1,
)

user.save()