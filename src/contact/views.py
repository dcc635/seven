from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import ContactForm


def home(request):
    title = "Contact Us"
    form = ContactForm(request.POST or None)
    confirm_message = None

    if form.is_valid():
        comment = form.cleaned_data['comment']
        name = form.cleaned_data['name']
        email_subject = 'Message to Seven.com'
        email_message = '{comment} {name}'.format(**locals())
        email_from = form.cleaned_data['email']
        email_to = [settings.EMAIL_HOST_USER]
        print(email_subject, email_message, email_from, email_to)
        # store the message
        send_mail(
            email_subject,
            email_message,
            email_from,
            email_to,
            fail_silently=True,
        )
        title = 'Thank you'
        form = None
        confirm_message = """
Thank you for your message. We have received it and we are reviewing it.
"""

    context = {
        'title': title,
        'form': form,
        'confirm_message': confirm_message,
    }

    template = 'contact.html'
    return render(request, template, context)
