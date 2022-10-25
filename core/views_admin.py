from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from core.forms import AddStudentForm, EditStudentForm
from core.models import CustomUser, Courses, Staffs, Subject, Students, SessionYear


@login_required
def admin_home(request):
    return render(request, 'admin_templates/home_content.html')


@login_required
def add_staff(request):
    return render(request, 'admin_templates/add_staff_template.html')


@login_required
def add_staff_save(request):
    if request.method != 'POST':
        return HttpResponse('<h2>Método não Permitido</h2>')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        try:
            user = CustomUser.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=first_name,
                last_name=last_name,
                user_type=2,
            )
            user.staffs.address = address
            user.save()

            messages.success(request, 'Funcionário adicionado com Sucesso!')
            return HttpResponseRedirect(reverse('add_staff'))
        except Exception as e:
            messages.error(request, f'Falha ao adicionar Funcionário\n{e}')
            return HttpResponseRedirect(reverse('add_staff'))


@login_required
def add_course(request):
    return render(request, 'admin_templates/add_course_template.html')


@login_required
def add_course_save(request):
    if request.method != 'POST':
        return HttpResponse('<h2>Método não Permitido</h2>')
    else:
        course = request.POST.get('course')
        try:
            course = Courses(course_name=course)
            course.save()
            messages.success(request, 'Curso adicionado com Sucesso!')
            return HttpResponseRedirect(reverse('add_course'))
        except Exception as e:
            messages.error(request, f'Falha ao adicionar Curso\n{e}')
            return HttpResponseRedirect(reverse('add_course'))


@login_required
def add_student(request):
    form = AddStudentForm()
    return render(
        request,
        'admin_templates/add_student_template.html',
        {'form': form}
    )


@login_required
def add_student_save(request):
    if request.method != 'POST':
        return HttpResponse('<h2>Método não Permitido</h2>')
    else:
        form = AddStudentForm(request.POST, request.FILES)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Endereço
            # address = form.cleaned_data['address']
            cep = form.cleaned_data['cep']
            logradouro = form.cleaned_data['logradouro']
            bairro = form.cleaned_data['bairro']
            localidade = form.cleaned_data['localidade']
            uf = form.cleaned_data['uf']
            numero = form.cleaned_data['numero']
            complemento = form.cleaned_data['complemento']

            session_year_id = form.cleaned_data['session_year_id']
            course_id = form.cleaned_data['course']
            gender = form.cleaned_data['gender']
            profile_pic = request.FILES['profile_pic']
            fs = FileSystemStorage()
            filename = fs.save(profile_pic.name, profile_pic)
            profile_pic_url = fs.url(filename)

            try:
                user = CustomUser.objects.create_user(
                    username=username,
                    password=password,
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    user_type=3,
                )
                # user.students.address = address
                user.students.address = cep
                user.students.address = logradouro
                user.students.address = bairro
                user.students.address = localidade
                user.students.address = uf
                user.students.address = numero
                user.students.address = complemento

                user.students.session_year_id = SessionYear.objects.get(id=session_year_id)
                user.students.course_id = Courses.objects.get(id=course_id)
                user.students.gender = gender
                user.students.profile_pic = profile_pic_url
                user.save()

                messages.success(request, 'Aluno adicionado com Sucesso!')
                return HttpResponseRedirect(reverse('add_student'))
            except Exception as e:
                print(e)
                messages.error(request, f'Falha ao adicionar Aluno\n{e}')
                return HttpResponseRedirect(reverse('add_student'))
        else:
            form = AddStudentForm(request.POST)
            return render(
                request,
                'admin_templates/add_student_template.html',
                {'form': form}
            )


@login_required
def add_subject(request):
    courses = Courses.objects.all()
    staffs = CustomUser.objects.filter(user_type=2)
    return render(
        request,
        'admin_templates/add_subject_template.html',
        {'courses': courses, 'staffs': staffs}
    )


@login_required
def add_subject_save(request):
    if request.method != 'POST':
        return HttpResponse('<h2>Método não Permitido</h2>')
    else:
        subject = request.POST.get('subject')
        course_id = request.POST.get('course')
        course = Courses.objects.get(id=course_id)
        staff_id = request.POST.get('staff')
        staff = CustomUser.objects.get(id=staff_id)

        try:
            subject_model = Subject(
                subject_name=subject,
                course_id=course,
                staff_id=staff,
            )
            subject_model.save()
            messages.success(request, 'Disciplina adicionada com Sucesso!')
            return HttpResponseRedirect(reverse('add_subject'))
        except Exception as e:
            messages.error(request, f'Falha ao adicionar Disciplina\n{e}')
            return HttpResponseRedirect(reverse('add_subject'))


@login_required
def manage_staff(request):
    staffs = Staffs.objects.all()
    return render(
        request,
        'admin_templates/manage_staff.html',
        {'staffs': staffs},
    )


@login_required
def manage_student(request):
    students = Students.objects.all()
    return render(
        request,
        'admin_templates/manage_student.html',
        {'students': students},
    )


@login_required
def manage_course(request):
    courses = Courses.objects.all()
    return render(
        request,
        'admin_templates/manage_courses.html',
        {'courses': courses},
    )


@login_required
def manage_subject(request):
    subjects = Subject.objects.all()
    return render(
        request,
        'admin_templates/manage_subject.html',
        {'subjects': subjects},
    )


@login_required
def edit_staff(request, staff_id):
    staff = Staffs.objects.get(admin=staff_id)
    return render(
        request,
        'admin_templates/edit_staff_template.html',
        {'staff': staff, 'id': staff_id}
    )


@login_required
def edit_staff_save(request):
    if request.method != 'POST':
        return HttpResponse('<h2>Método não Permitido</h2>')
    else:
        staff_id = request.POST.get('staff_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        address = request.POST.get('address')

        try:
            user = CustomUser.objects.get(id=staff_id)
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.username = username
            user.save()

            staff_model = Staffs.objects.get(admin=staff_id)
            staff_model.address = address
            staff_model.save()

            messages.success(request, 'Funcionário alterado com Sucesso!')
            return HttpResponseRedirect(reverse('edit_staff', kwargs={'staff_id': staff_id}))
        except Exception as e:
            print(e)
            messages.error(request, 'Falha ao alterar Funcionário')
            return HttpResponseRedirect(reverse('edit_staff', kwargs={'staff_id': staff_id}))


@login_required
def edit_student(request, student_id):
    request.session['student_id'] = student_id  # Quando editar estudante, será armazenado o id do estudante no backend
    student = Students.objects.get(admin=student_id)
    form = EditStudentForm()
    form.fields['first_name'].initial = student.admin.first_name
    form.fields['last_name'].initial = student.admin.last_name
    form.fields['username'].initial = student.admin.username
    form.fields['email'].initial = student.admin.email

    # form.fields['address'].initial = student.address
    form.fields['cep'].initial = student.cep
    form.fields['logradouro'].initial = student.logradouro
    form.fields['bairro'].initial = student.bairro
    form.fields['localidade'].initial = student.localidade
    form.fields['uf'].initial = student.uf
    form.fields['numero'].initial = student.numero
    form.fields['complemento'].initial = student.complemento

    form.fields['course'].initial = student.course_id.id
    form.fields['gender'].initial = student.gender
    form.fields['session_year_id'].initial = student.session_year_id
    form.fields['profile_pic'].initial = student.profile_pic
    return render(
        request,
        'admin_templates/edit_student_template.html',
        {'form': form, 'id': student_id, 'username': student.admin.username}
    )


@login_required
def edit_student_save(request):
    if request.method != 'POST':
        return HttpResponse('<h2>Método não Permitido</h2>')
    else:
        student_id = request.session.get('student_id')
        if student_id is None:
            return HttpResponseRedirect(reverse('manage_student'))

        form = EditStudentForm(request.POST, request.FILES)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']

            # Endereço
            # address = form.cleaned_data['address']
            cep = form.cleaned_data['cep']
            logradouro = form.cleaned_data['logradouro']
            bairro = form.cleaned_data['bairro']
            localidade = form.cleaned_data['localidade']
            uf = form.cleaned_data['uf']
            numero = form.cleaned_data['numero']
            complemento = form.cleaned_data['complemento']

            session_year_id = form.cleaned_data['session_year_id']
            course_id = form.cleaned_data['course']
            gender = form.cleaned_data['gender']

            # Se tiver uma imagem carregada, atualiza.
            # Senão mantem a que imagem que está!
            if request.FILES.get('profile_pic', False):
                profile_pic = request.FILES['profile_pic']
                print(f'Name {profile_pic.name}\nSize {profile_pic.size}')
                fs = FileSystemStorage()
                filename = fs.save(profile_pic.name, profile_pic)
                profile_pic_url = fs.url(filename)
            else:
                profile_pic_url = None

            try:
                user = CustomUser.objects.get(id=student_id)
                user.first_name = first_name
                user.last_name = last_name
                user.email = email
                user.username = username
                user.save()

                student = Students.objects.get(admin=student_id)

                # student.address = address
                student.cep = cep
                student.logradouro = logradouro
                student.bairro = bairro
                student.localidade = localidade
                student.uf = uf
                student.numero = numero
                student.complemento = complemento

                student.gender = gender
                student.session_year_id = SessionYear.objects.get(id=session_year_id)
                if profile_pic_url is not None:
                    student.profile_pic = profile_pic_url
                course = Courses.objects.get(id=course_id)
                student.course_id = course
                student.save()
                del request.session['student_id']

                messages.success(request, 'Aluno alterado com Sucesso!')
                return HttpResponseRedirect(reverse('edit_student', kwargs={'student_id': student_id}))
            except Exception as e:
                messages.error(request, f'Falha ao alterar Aluno\n{e}')
                return HttpResponseRedirect(reverse('edit_student', kwargs={'student_id': student_id}))
        else:
            form = EditStudentForm(request.POST)
            student = Students.objects.get(admin=student_id)
            return render(
                request,
                'admin_templates/edit_student_template.html',
                {'form': form, 'id': student_id, 'username': student.admin.username}
            )


@login_required
def edit_subject(request, subject_id):
    subject = Subject.objects.get(id=subject_id)
    courses = Courses.objects.all()
    staffs = CustomUser.objects.filter(user_type=2)
    return render(
        request,
        'admin_templates/edit_subject_template.html',
        {
            'subject': subject,
            'courses': courses,
            'staffs': staffs,
            'id': subject_id,
        }
    )


@login_required
def edit_subject_save(request):
    if request.method != 'POST':
        return HttpResponse('<h2>Método não Permitido</h2>')
    else:
        subject_id = request.POST.get('subject_id')
        subject_name = request.POST.get('subject_name')
        staff_id = request.POST.get('staff')
        course_id = request.POST.get('course')

        try:
            subject = Subject.objects.get(id=subject_id)
            subject.subject_name = subject_name
            staff = CustomUser.objects.get(id=staff_id)
            subject.staff_id = staff
            course = Courses.objects.get(id=course_id)
            subject.course_id = course
            subject.save()

            messages.success(request, 'Disciplina alterado com Sucesso!')
            return HttpResponseRedirect(reverse('edit_subject', kwargs={'subject_id': subject_id}))
        except Exception as e:
            messages.error(request, f'Falha ao alterar Disciplina\n{e}')
            return HttpResponseRedirect(reverse('edit_subject', kwargs={'subject_id': subject_id}))


@login_required
def edit_course(request, course_id):
    course = Courses.objects.get(id=course_id)
    return render(
        request,
        'admin_templates/edit_course_template.html',
        {'course': course, 'id': course_id}
    )


@login_required
def edit_course_save(request):
    if request.method != 'POST':
        return HttpResponse('<h2>Método não Permitido</h2>')
    else:
        course_id = request.POST.get('course_id')
        course_name = request.POST.get('course_name')

        try:
            course = Courses.objects.get(id=course_id)
            course.course_name = course_name
            course.save()
            messages.success(request, 'Curso alterado com Sucesso!')
            return HttpResponseRedirect(reverse('edit_course', kwargs={'course_id': course_id}))
        except Exception as e:
            messages.error(request, f'Falha ao alterar Curso\n{e}')
            return HttpResponseRedirect(reverse('edit_course', kwargs={'course_id': course_id}))


@login_required
def manage_session(request):
    return render(request, 'admin_templates/manage_session_template.html')


def add_session_save(request):
    if request.method != 'POST':
        return HttpResponseRedirect(reverse('manage_session'))
    else:
        session_start = request.POST.get('session_start')
        session_end = request.POST.get('session_end')
        try:
            session_year = SessionYear(
                session_start_year=session_start,
                session_end_year=session_end
            )
            session_year.save()
            messages.success(request, 'Data adicionada com Sucesso!')
            return HttpResponseRedirect(reverse('manage_session'))
        except Exception as e:
            messages.error(request, f'Falha ao adicionar Data\n{e}')
            return HttpResponseRedirect(reverse('manage_session'))

