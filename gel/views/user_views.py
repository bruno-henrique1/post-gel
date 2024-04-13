from django.shortcuts import render, redirect
from gel.forms import RegisterForm
from django.contrib import messages, auth
from django.contrib.auth.forms import AuthenticationForm
def register(request):
    form = RegisterForm()
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            messages.success(request,'Usuário registrado com sucesso!')
            form.save()
            return redirect('gel:index')

    return render(request,'gel/register.html',
                  {
                      'form': form
                  })

def login_views(request):
    form = AuthenticationForm(request)
    if request.method == 'POST': 
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            messages.success(request,'Usuário logado com sucesso!')
            auth.login(request,user)
            print(user)
    return render(request,'gel/login.html',
                  {
                      'form': form
                  })

def logout_views(request):
    auth.logout(request)
    return redirect('gel:login')