from django.shortcuts import render, redirect
from gel.forms import RegisterForm, RegisterUpdateForm
from django.contrib import messages, auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

def register(request):
    form = RegisterForm()
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            messages.success(request,'Usuário registrado com sucesso!')
            form.save()
            return redirect('gel:login')

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
            return redirect('gel:index')
        messages.error(request,'Login inválido!')
    return render(request,'gel/login.html',
                  {
                      'form': form
                  })
@login_required(login_url='gel:register')
def logout_views(request):
    auth.logout(request)
    return redirect('gel:login')

@login_required(login_url='gel:register')
def update_views(request):
    form = RegisterUpdateForm(instance=request.user)
    if request.method != 'POST':
        return render(
        request,
        'gel/update.html',
        {
            'form':form
        })
    
    form = RegisterUpdateForm(data=request.POST,instance=request.user)

    if not form.is_valid():
        return render(
        request,
        'gel/update.html',
        {
            'form':form
        })
    
    form.save()

    return redirect('gel:update')