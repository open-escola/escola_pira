from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def staff_home(request):
    return render(request, 'staff_templates/home_content.html')
