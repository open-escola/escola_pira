from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from core.models import CustomUser, Courses, Staffs, Subject, Students


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

            messages.success(request, "Funcionário adicionado com Sucesso!")
            return HttpResponseRedirect('/add_staff')
        except Exception as e:
            print(e)
            messages.error(request, "Falha ao adicionar Funcionário")
            return HttpResponseRedirect('/add_staff')


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
            return HttpResponseRedirect('/add_course')
        except Exception as e:
            print(e)
            messages.error(request, 'Falha ao adicionar Curso')
            return HttpResponseRedirect('/add_course')


@login_required
def add_student(request):
    courses = Courses.objects.all()
    return render(
        request,
        'admin_templates/add_student_template.html',
        {"courses": courses}
    )


@login_required
def add_student_save(request):
    if request.method != 'POST':
        return HttpResponse('<h2>Método não Permitido</h2>')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        session_start = request.POST.get('session_start')
        session_end = request.POST.get('session_end')
        course_id = request.POST.get('course')
        gender = request.POST.get('gender')

        profile_pic = request.FILES['profile_pic']
        print(f'ddd {profile_pic.name} ddd {profile_pic.size}')
        fs = FileSystemStorage()
        filename = fs.save(profile_pic.name, profile_pic)
        profile_pic_url = fs.url(filename)

        # session_start = datetime.datetime.strptime(session_start, '%Y-%m-%d').strftime('%Y-%m-%d')
        # session_end = datetime.datetime.strptime(session_end, '%Y-%m-%d').strftime('%Y-%m-%d')

        try:
            user = CustomUser.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=first_name,
                last_name=last_name,
                user_type=3,
            )
            user.students.address = address
            user.students.session_start_year = session_start
            user.students.session_end_year = session_end
            user.students.course_id = Courses.objects.get(id=course_id)
            user.students.gender = gender
            user.students.profile_pic = profile_pic_url
            user.save()

            messages.success(request, 'Aluno adicionado com Sucesso!')
            return HttpResponseRedirect('/add_student')
        except Exception as e:
            messages.error(request, f'Falha ao adicionar Aluno | Erro: {e}')
            return HttpResponseRedirect('/add_student')


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
            return HttpResponseRedirect('/add_subject')
        except Exception as e:
            print(e)
            messages.error(request, 'Falha ao adicionar Disciplina')
            return HttpResponseRedirect('/add_subject')


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
        {'staff': staff}
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
            return HttpResponseRedirect(f'/edit_staff/{staff_id}')
        except Exception as e:
            print(e)
            messages.error(request, 'Falha ao alterar Funcionário')
            return HttpResponseRedirect(f'/edit_staff/{staff_id}')


@login_required
def edit_student(request, student_id):
    student = Students.objects.get(admin=student_id)
    courses = Courses.objects.all()  # Preciso enviar a informação dos cursos para que seja possível alterar o aluno
    # de classe
    print(student.session_end_year)
    return render(
        request,
        'admin_templates/edit_student_template.html',
        {'student': student, 'courses': courses}
    )


@login_required
def edit_student_save(request):
    if request.method != 'POST':
        return HttpResponse('<h2>Método não Permitido</h2>')
    else:
        student_id = request.POST.get('student_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        address = request.POST.get('address')
        course_id = request.POST.get('course')
        gender = request.POST.get('gender')
        session_start = request.POST.get('session_start')
        session_end = request.POST.get('session_end')

        # Se tiver uma imagem carregada, atualiza.
        # Senão mantem a que imagem que está!
        if request.FILES['profile_pic']:
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
            student.address = address
            student.gender = gender
            student.session_start = session_start
            student.session_end = session_end
            if profile_pic_url is not None:
                student.profile_pic = profile_pic_url
            course = Courses.objects.get(id=course_id)
            student.course_id = course
            student.save()

            messages.success(request, 'Aluno alterado com Sucesso!')
            return HttpResponseRedirect(f'/edit_student/{student_id}')
        except Exception as e:
            messages.error(request, 'Falha ao alterar Aluno')
            messages.error(request, e)
            return HttpResponseRedirect(f'/edit_student/{student_id}')


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
            return HttpResponseRedirect(f'/edit_subject/{subject_id}')
        except Exception as e:
            messages.error(request, 'Falha ao alterar Disciplina')
            messages.error(request, e)
            return HttpResponseRedirect(f'/edit_subject/{subject_id}')


@login_required
def edit_course(request, course_id):
    course = Courses.objects.get(id=course_id)
    return render(
        request,
        'admin_templates/edit_course_template.html',
        {'course': course}
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
            return HttpResponseRedirect(f'/edit_course/{course_id}')
        except Exception as e:
            messages.error(request, 'Falha ao alterar Curso')
            messages.error(request, e)
            return HttpResponseRedirect(f'/edit_course/{course_id}')
