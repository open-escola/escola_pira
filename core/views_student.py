from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def student_home(request):
    return render(request, 'student_templates/home_content.html')
