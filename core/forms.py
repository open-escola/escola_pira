from django import forms

from core.models import Courses, SessionYear


# Forms
class DateInput(forms.DateInput):
    input_type = 'date'


class AddStudentForm(forms.Form):
    first_name = forms.CharField(
        label='Primeiro Nome',
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Primeiro Nome'})
    )
    last_name = forms.CharField(
        label='Sobrenome',
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    username = forms.CharField(
        label='Username',
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label='E-mail',
        max_length=50,
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label='Password',
        max_length=50,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    address = forms.CharField(
        label='Endereço',
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    course_choices = []
    try:
        courses = Courses.objects.all()
        for course in courses:
            course_choices.append((course.id, course.course_name))
    except Exception as e:
        print(e)
    course = forms.ChoiceField(
        label='Curso',
        choices=course_choices,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    gender_choices = (
        ('Masculino', 'Masculino'),
        ('Feminino', 'Feminino')
    )
    gender = forms.ChoiceField(
        label='Gênero',
        choices=gender_choices,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    session_choices = []
    try:
        sessions = SessionYear.objects.all()
        for session in sessions:
            session_choices.append(
                (session.id, '{} até {}'.format(session.session_start_year, session.session_end_year)))
    except Exception as e:
        print(e)

    session_year_id = forms.ChoiceField(
        label='session year',
        choices=session_choices,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    profile_pic = forms.FileField(
        label='profile_pic',
        max_length=50,
        widget=forms.FileInput(attrs={'class': 'form-control'})
    )

class EditStudentForm(forms.Form):
    first_name = forms.CharField(label='Primeiro Nome', max_length=50,
                                 widget=forms.TextInput(
                                     attrs={'class': 'form-control', 'placeholder': 'Primeiro Nome'}))
    last_name = forms.CharField(label='Sobrenome', max_length=50,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label='Username', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='E-mail', max_length=50, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    address = forms.CharField(label='Endereço', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))

    course_choices = []
    try:
        courses = Courses.objects.all()
        for course in courses:
            course_choices.append((course.id, course.course_name))
    except Exception as e:
        print(e)
    course = forms.ChoiceField(label='Curso', choices=course_choices,
                               widget=forms.Select(attrs={'class': 'form-control'}))

    gender_choices = (
        ('Masculino', 'Masculino'),
        ('Feminino', 'Feminino')
    )
    gender = forms.ChoiceField(label='Gênero', choices=gender_choices,
                               widget=forms.Select(attrs={'class': 'form-control'}))

    session_choices = []
    try:
        sessions = SessionYear.objects.all()
        for session in sessions:
            session_choices.append(
                (session.id, f'{session.session_start_year} até {session.session_end_year}'))
    except Exception as e:
        print(e)
    session_year_id = forms.ChoiceField(label='session year', choices=session_choices,
                                        widget=forms.Select(attrs={'class': 'form-control'}))
    profile_pic = forms.FileField(label='profile_pic', max_length=50,
                                  widget=forms.FileInput(attrs={'class': 'form-control'}), required=False)
