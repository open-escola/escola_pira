from django.test import TestCase

from core.models import Admin, CustomUser


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


class StudentTestCase(TestCase):
    def setUp(self):

        CustomUser.objects.create_user(
            username='aluno1',
            password='12345',
            email='aluno1@email.com',
            first_name='Aluno',
            last_name='Test',
            user_type=3,
        ).save()

    def test_student_created_correctly(self):
        """Usuário contém informações corretas e é aluno"""
        user2 = CustomUser.objects.get(username='aluno1')

        self.assertEqual(CustomUser.get_full_name(user2), 'Aluno Test')
        self.assertEqual(user2.user_type, '3')


class StaffTestCase(TestCase):
    def setUp(self):
        CustomUser.objects.create_user(
            username='staff1',
            password='12345',
            email='staff1@email.com',
            first_name='Staff',
            last_name='Test',
            user_type=2,
        ).save()

    def test_staff_created_correctly(self):
        """Usuário contém informações corretas e é funcionario"""
        user3 = CustomUser.objects.get(username='staff1')

        self.assertEqual(CustomUser.get_full_name(user3), 'Staff Test')
        self.assertEqual(user3.user_type, '2')
