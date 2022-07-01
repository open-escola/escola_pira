# class StudentTestCase(TestCase):
#     def setUp(self):
#         CustomUser.objects.create_user(
#             username='aluno1',
#             password='12345',
#             email='aluno1@email.com',
#             first_name='Aluno',
#             last_name='Test',
#             user_type=3,
#         ).save()
#
#     def test_student_created_correctly(self):
#         """Usuário contém informações corretas e é aluno"""
#         user2 = CustomUser.objects.get(username='aluno1')
#
#         self.assertEqual(CustomUser.get_full_name(user2), 'Aluno Test')
#         self.assertEqual(user2.user_type, '3')
