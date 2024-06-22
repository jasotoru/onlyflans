from django.shortcuts import render
from .models import Flan
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ContactFormForm

def index(request):
    flanes = Flan.objects.all()
    return render(request, 'index.html', {'flanes': flanes})

def about(request):
    return render(request, 'about.html')

@login_required
def welcome(request):
    flanes = Flan.objects.filter(is_private=True)
    username = request.user.username
    return render(request, 'welcome.html', {'flanes': flanes ,'username': username})

def contacto(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exito')
    else:
        form = ContactFormForm()
    return render(request, 'contacto.html', {'form': form})

def exito(request):
    return render(request, 'exito.html')

