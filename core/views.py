from django.contrib.auth import login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from core.email_backend import EmailBackend


# Create your views here.


def show_demo_page(request):
    return render(request, 'demo.html')


def show_login_page(request):
    return render(request, 'login_page.html')


def do_login(request):
    if request.method != 'POST':
        return HttpResponse('<h2>Method Not Allowed</h2>')
    else:
        user = EmailBackend.authenticate(request, username=request.POST.get('email'),
                                         password=request.POST.get('password'))
        print(user)
        if user is not None:
            login(request, user)
            if user.user_type == '1':
                return HttpResponseRedirect('/admin_home')
            elif user.user_type == '2':
                return HttpResponseRedirect(reverse('staff_home'))
            else:
                return HttpResponseRedirect(reverse('student_home'))
        else:
            #messages.error(request, "Invalid Login Details")
            print('Merda')
            return HttpResponseRedirect("/")


def get_user_detail(request):
    if request.user is not None:
        return HttpResponse("Email : " + request.user.email + " UserType : ")
        # + request.user.user_type)
    else:
        return HttpResponse('<h2>por favor, faça login </h2>')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')
