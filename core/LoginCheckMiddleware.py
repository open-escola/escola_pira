from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class LoginCheckMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        module_name = view_func.__module__
        user = request.user
        if user.is_authenticated:
            if user.user_type == '1':
                if module_name == 'core.views':
                    pass
                elif module_name == 'core.views_admin':
                    pass
                else:
                    return HttpResponseRedirect(reverse('admin_home'))

            if user.user_type == '2':
                if module_name == 'core.views':
                    pass
                elif module_name == 'core.views_staff':
                    pass
                else:
                    return HttpResponseRedirect(reverse('staff_home'))

            if user.user_type == '3':
                if module_name == 'core.views':
                    pass
                elif module_name == 'core.views_student':
                    pass
                else:
                    return HttpResponseRedirect(reverse('student_home'))

        else:
            if request.path == reverse('login') or request.path == reverse('do_login'):
                pass
            else:
                return HttpResponseRedirect(reverse('login'))
