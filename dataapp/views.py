from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from dataapp.models import Patient
from dataapp.forms import PatientsForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate

# Create your views here.
def index(request):
    return render(request, 'index.html')

@login_required
def create(request):
    form = PatientsForm(request.POST)
    if request.method == 'POST': 
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
        return redirect('retrieve')
    else:
        form = PatientsForm()
    return render(request, 'dataentry.html', {'form': form})

@login_required
def retrieve(request):
    records = Patient.objects.all()
    return render(request, 'retrieve.html', {'records': records})

@login_required
def update(request, id):
    objects = Patient.objects.get(id=id)
    form = PatientsForm(instance=objects)
    if request.method == 'POST': 
        form = PatientsForm(request.POST, instance=objects)
        if form.is_valid():
            form.save()
        else:
            form = PatientsForm()
        return redirect('retrieve')
    return render(request, 'update.html', {'form': form})

@login_required
def delete(request, id):
    info = Patient.objects.get(id=id)
    if request.method == 'POST': 
        info.delete()
        return redirect('retrieve')
    return render(request, 'delete.html')

# def login(request, id):
#    return render(request, 'login.html')
def register(request):
    form = UserCreationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password2')
            form.save()
            user = authenticate(username = username,password=password)
            login(request, user)
            return redirect('retrieve')
    return render(request, 'registration/register.html', {'form' : form})









