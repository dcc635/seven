from django.shortcuts import render

from .forms import ContactForm


def home(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():
        print(form.cleaned_data['email'])
        print(request.POST)

    context = locals()
    template = 'contact.html'
    return render(request, template, context)
