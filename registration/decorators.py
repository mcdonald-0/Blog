from django.shortcuts import redirect


def unauthenticated_user(view_func):
    def wrapper(request, *args, **kwargs):
        
        if request.user.is_authenticated:
            return redirect('blog:home')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper

def redirect_unauthenticated_user_to_login(view_func):
    def wrapper(request, *args, **kwargs):
        
        if request.user.is_authenticated:
            return redirect('blog:home')
        else:
            return redirect('registration:login')

    return wrapper