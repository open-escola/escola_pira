from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from core.models import CustomUser, Courses, Staffs, Subject, Students


def admin_home(request):
    return render(request, 'admin_templates/home_content.html')


def add_staff(request):
    return render(request, 'admin_templates/add_staff_template.html')


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


def add_course(request):
    return render(request, 'admin_templates/add_course_template.html')


def add_course_save(request):
    if request.method != 'POST':
        return HttpResponse('<h2>Método não Permitido</h2>')
    else:
        course = request.POST.get('course')

        try:
            course_model = Courses(course_name=course)
            course_model.save()
            messages.success(request, "Curso adicionado com Sucesso!")
            return HttpResponseRedirect('/add_course')
        except Exception as e:
            print(e)
            messages.error(request, "Falha ao adicionar Curso")
            return HttpResponseRedirect('/add_course')


def add_student(request):
    courses = Courses.objects.all()
    return render(
        request,
        'admin_templates/add_student_template.html',
        {"courses": courses}
    )


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
            user.save()

            messages.success(request, "Aluno adicionado com Sucesso!")
            return HttpResponseRedirect('/add_student')
        except Exception as e:
            print(e)
            messages.error(request, "Falha ao adicionar Aluno")
            return HttpResponseRedirect('/add_student')


def add_subject(request):
    courses = Courses.objects.all()
    staffs = CustomUser.objects.filter(user_type=2)
    return render(
        request,
        'admin_templates/add_subject_template.html',
        {
            "courses": courses,
            "staffs": staffs,
        }
    )


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


def manage_staff(request):
    staffs = Staffs.objects.all()
    return render(
        request,
        'admin_templates/manage_staff.html',
        {'staffs': staffs},
    )


def manage_student(request):
    students = Students.objects.all()
    return render(
        request,
        'admin_templates/manage_student.html',
        {'students': students},
    )


def manage_course(request):
    courses = Courses.objects.all()
    return render(
        request,
        'admin_templates/manage_courses.html',
        {'courses': courses},
    )


def manage_subject(request):
    subjects = Subject.objects.all()
    return render(
        request,
        'admin_templates/manage_subject.html',
        {'subjects': subjects},
    )


def edit_staff(request, staff_id):
    staff = Staffs.objects.get(admin=staff_id)
    return render(
        request,
        'admin_templates/edit_staff_template.html',
        {'staff': staff}
    )


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
            messages.error(request, 'Falha ao adicionar Disciplina')
            return HttpResponseRedirect(f'/edit_staff/{staff_id}')


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

        try:
            user = CustomUser.objects.get(id=student_id)
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.username = username
            user.save()

            student_model = Students.objects.get(admin=student_id)
            student_model.address = address
            student_model.gender = gender
            student_model.session_start = session_start
            student_model.session_end = session_end
            course = Courses.objects.get(id=course_id)
            student_model.course_id = course
            student_model.save()

            messages.success(request, 'Aluno alterado com Sucesso!')
            return HttpResponseRedirect(f'/edit_student/{student_id}')
        except Exception as e:
            print(e)
            messages.error(request, 'Falha ao alterar Aluno')
            return HttpResponseRedirect(f'/edit_student/{student_id}')
