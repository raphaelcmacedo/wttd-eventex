from django.conf import settings
from django.contrib import messages
from django.core import mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string

from eventex.subscriptions.forms import SubscriptionForm


def _send_email(form):
    subject = 'Confirmação de inscrição'
    message = render_to_string('subscriptions/subscription_email.txt', form.cleaned_data)
    from_email = settings.DEFAULT_FROM_EMAIL
    to = [from_email, form.cleaned_data['email']]
    mail.send_mail(subject, message, from_email, to)


def subscribe(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new (request)


def create(request):
    form = SubscriptionForm(request.POST)
    if not form.is_valid():
        return render(request, 'subscriptions/subscription_form.html', {"form": form})

    _send_email(form)
    messages.success(request, 'Inscrição realizada com sucesso')
    return HttpResponseRedirect('/inscricao/')


def new(request):
    context = {'form': SubscriptionForm()}
    return render(request, 'subscriptions/subscription_form.html', context)

