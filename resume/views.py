from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm
# Create your views here.

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'resume/success.html')

    form = ContactForm()

    return render(request, 'resume/home.html', {'form': form})

