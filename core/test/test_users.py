from django.test import TestCase

from core.models import CustomUser


# Create your tests here.


class UserTestCase(TestCase):
    def setUp(self):
        CustomUser.objects.create_user(
            username='sseber',
            password='12345',
            email='sseber@gmail.com',
            first_name='Samile',
            last_name='Seber',
            user_type=1,
        )

    def test_user_created_correctly(self):
        """Usuário contém informações corretas"""
        user1 = CustomUser.objects.get(username='sseber')
        print(CustomUser.get_full_name(user1))

        self.assertEqual(CustomUser.get_full_name(user1), 'Samile Seber')
