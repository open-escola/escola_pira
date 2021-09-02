from django.contrib.auth import login, logout
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from core.email_backend import EmailBackend


# Create your views here.
def go_index(request):
    return render(request, 'index.html')


def go_index2(request):
    return render(request, 'index2.html')


def go_index3(request):
    return render(request, 'index3.html')


# LOGIN
def go_login_page(request):
    return render(request, 'login/login.html')


def go_login_forgot(request):
    return render(request, 'login/forgot-password.html')


def go_register(request):
    return render(request, 'login/register.html')


def go_recovery(request):
    return render(request, 'login/recovery-password.html')


def do_login(request):
    if request.method != 'POST':
        return HttpResponse('<h2>Método não Permitido</h2>')
    else:
        user = EmailBackend.authenticate(
            request,
            username=request.POST.get('email'),
            password=request.POST.get('password')
        )
        if user is not None:
            login(request, user)
            if user.user_type == '1':
                #return HttpResponseRedirect('/')
                return HttpResponseRedirect('/admin_home')
            elif user.user_type == '2':
                return HttpResponseRedirect(reverse('staff_home'))
            elif user.user_type == '3':
                return HttpResponseRedirect(reverse('student_home'))
            else:
                return HttpResponse('<h2>Deu ruim no login 1</h2>')
        else:
            messages.error(request, 'Invalid Login Details')
            return HttpResponseRedirect('/')
            #return HttpResponse('<h2>Deu ruim no login 2</h2>')


def get_user_detail(request):
    if request.user is not None:
        return HttpResponse(f'<h2>Email: {request.user.email} | UserType: {request.user.user_type}</h2>')
    else:
        return HttpResponse('<h2>Por favor, faça login!</h2>')


def do_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
