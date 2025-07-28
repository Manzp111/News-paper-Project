from functools import wraps
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import user_passes_test

def SupervisorRequired():
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            user= request.user
            if user.is_authenticated and user.role== 'supervisor':
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponseForbidden("You do not have permission to access this page.")
        return _wrapped_view
    return decorator

def AuthorRequired():
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            user = request.user
            if user.is_authenticated and user.role == 'author' or user.role == 'supervisor':
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponseForbidden("You do not have permission to access this page.")
        return _wrapped_view
    return decorator





