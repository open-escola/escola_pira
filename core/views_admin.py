import datetime
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
