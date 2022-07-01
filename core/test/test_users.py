from django.test import TestCase

from core.models import CustomUser


# Create your tests here.
class AdminTestCase(TestCase):
    def setUp(self):
        CustomUser.objects.create_user(
            username='sseber',
            password='12345',
            email='sseber@gmail.com',
            first_name='Samile',
            last_name='Seber',
            user_type=1,
        ).save()

    def test_admin_created_correctly(self):
        """Usuário contém informações corretas e é admin"""
        user1 = CustomUser.objects.get(username='sseber')

        self.assertEqual(CustomUser.get_full_name(user1), 'Samile Seber')
        self.assertEqual(user1.user_type, '1')


class StaffTestCase(TestCase):
    def setUp(self):
        CustomUser.objects.create_user(
            username='michelmetran',
            password='12345',
            email='michelmetran@gmail.com',
            first_name='Michel',
            last_name='Metran',
            user_type=2,
        ).save()

    def test_staff_created_correctly(self):
        """Usuário contém informações corretas e é funcionario"""
        user2 = CustomUser.objects.get(username='michelmetran')

        self.assertEqual(CustomUser.get_full_name(user2), 'Michel Metran')
        self.assertEqual(user2.user_type, '2')
