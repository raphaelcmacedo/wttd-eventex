from django.core import mail
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages


# Create your views here.
from django.template.loader import render_to_string

from eventex.subscriptions.forms import SubscriptionForm

def send_email(form):
    subject = 'Confirmação de inscrição'
    context = dict(name='Raphael Macedo', cpf='00000000000', email='raphaelcmacedo@hotmail.com',phone='(00) 00000-0000')
    message = render_to_string('subscriptions/subscription_email.txt', form.cleaned_data)
    from_email = 'contato@eventex.com.br'
    to = ['contato@eventex.com.br', form.cleaned_data['email']]
    mail.send_mail(subject, message, from_email, to)

def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            send_email(form)
            messages.success(request, 'Inscrição realizada com sucesso')
            return HttpResponseRedirect('/inscricao/')
        else:
            return render(request, 'subscriptions/subscription_form.html', {"form":form})
    else:
        context = {'form': SubscriptionForm()}
        return render(request, 'subscriptions/subscription_form.html', context)

