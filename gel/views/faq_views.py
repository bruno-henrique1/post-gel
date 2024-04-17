from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from gel.forms import register_faq
from django.contrib import messages

@login_required(login_url='gel:login')
def create_faq(request):
    form_action = reverse('gel:create_faq')

    if request.method == 'POST':
        form = register_faq(request.POST, request.FILES)

        context = {
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            contact = form.save(commit=False)
            contact.owner = request.user
            contact.save()
            messages.success(request,'Vistoria registrada, Obrigado!')
            return redirect('gel:index')

        return render(
            request,
            'gel/create_faq.html',
            context
        )

    context = {
        'form': register_faq(),
        'form_action': form_action,
    }

    return render(
        request,
        'gel/create_faq.html',
        context
    )





"""from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from gel.forms import register_faq
from gel.models import faq

def resgister_faq(request):
    form_action = reverse('gel:faq')

    if request.method == 'POST':
        form = register_faq(request.POST, request.FILES)

        context = {
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            contact = form.save(commit=False)
            contact.owner = request.user
            contact.save()
            return redirect('gel:update', faq_id=contact.pk)

        return render(
            request,
            'gel/register.html',
            context
        )

    context = {
        'form': register_faq(),
        'form_action': form_action,
    }

    return render(
        request,
        'gel/register.html',
        context
    )"""
