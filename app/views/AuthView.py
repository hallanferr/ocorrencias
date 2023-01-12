from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from app.forms.AuthForm import LoginForm

def login_view(request):
    loginForm = LoginForm()
    message = None
    if request.user.is_authenticated:
        return redirect('home_view')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        loginForm = LoginForm(request.POST)

        if loginForm.is_valid():
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                _next=request.GET.get('next')
                if _next is not None:
                    return redirect(_next)
                else:
                    return redirect("/login")
            else:
                message = {
                    'type': 'danger',
                    'text': 'Dados de usuário incorretos'
                }
    context = {
        'form': loginForm,
        'message': message,
        'title': 'Login',
        'button_text': 'Entrar'
    }

    return render(request, template_name='auth/auth.html', context=context, status=200)

def logout_view(request):
    logout(request)
    return redirect('/login')