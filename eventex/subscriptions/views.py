from django.conf import settings
from django.contrib import messages
from django.core import mail
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url
from django.template.loader import render_to_string

from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


def _send_email(subscription):
    subject = 'Confirmação de inscrição'
    message = render_to_string('subscriptions/subscription_email.txt', {"subscription":subscription})
    from_email = settings.DEFAULT_FROM_EMAIL
    to = [from_email, subscription.email]
    mail.send_mail(subject, message, from_email, to)


def new(request):
    if request.method == 'POST':
        return create(request)
    else:
        return empty_form (request)

def create(request):
    form = SubscriptionForm(request.POST)
    if not form.is_valid():
        return render(request, 'subscriptions/subscription_form.html', {"form": form})

    # Save on db
    #subscription = Subscription.objects.create(**form.cleaned_data)
    subscription = form.save()#possible to use save since now it's a ModelForm
    _send_email(subscription)

    return HttpResponseRedirect(resolve_url('subscriptions:detail',subscription.pk))


def empty_form(request):
    context = {'form': SubscriptionForm()}
    return render(request, 'subscriptions/subscription_form.html', context)


def detail(request, pk):
    try:
        subscription = Subscription.objects.get(pk = pk)
    except Subscription.DoesNotExist:
        raise Http404
    return render(request,  'subscriptions/subscription_detail.html',{'subscription':subscription})

