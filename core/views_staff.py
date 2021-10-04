import json

from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from core.models import Subject, Students, SessionYear, Attendance, AttendanceReport


@login_required
def staff_home(request):
    return render(request, 'staff_templates/home_content.html')


def staff_take_attendance(request):
    subjects = Subject.objects.filter(staff_id=request.user.id)
    session_years = SessionYear.objects.all()
    return render(request, 'staff_templates/staff_take_attendance.html',
                  {'subjects': subjects, 'session_years': session_years})


@csrf_exempt  # Dont need CRSF using AJAX
def get_students(request):
    subject_id = request.POST.get('subject')
    session_year = request.POST.get('session_year')

    subject = Subject.objects.get(id=subject_id)
    session = SessionYear.objects.get(id=session_year)
    students = Students.objects.filter(course_id=subject.course_id, session_year_id=session)
    print(students)
    students_data = serializers.serialize("python", students)
    list_data = []
    for student in students:
        data_small = {'id': student.admin.id, 'name': '{} {}'.format(student.admin.first_name, student.admin.last_name)}
        list_data.append(data_small)
    return JsonResponse(json.dumps(list_data), content_type="application/json", safe=False)


@csrf_exempt  # Dont need CRSF using AJAX
def save_attendance_data(request):
    student_ids = request.POST.get('student_ids')
    subject_id = request.POST.get('subject_id')
    attendance_date = request.POST.get('attendance_date')
    session_year_id = request.POST.get('session_year_id')

    subject_model = Subject.objects.get(id=subject_id)
    session_model = SessionYear.objects.get(id=session_year_id)

    json_students = json.loads(student_ids)

    try:
        attendance = Attendance(
            subject_id=subject_model,
            attendance_date=attendance_date,
            session_year_id=session_model
        )
        attendance.save()
        for stud in json_students:
            student = Students.objects.get(admin=stud['id'])
            attendance_report = AttendanceReport(
                student_id=student,
                attendance_id=attendance,
                status=stud['status']
            )
            attendance_report.save()
        return HttpResponse('Ok')

    except Exception as e:
        print(e)
        return HttpResponse('ERRO')
