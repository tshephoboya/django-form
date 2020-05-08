from django.shortcuts import render
from django.http import HttpResponse
from appTwo.models import User
from . import forms
# Create your views here.

def index(request):
    return render(request,'apptwo/index.html')

def users(request):
    form = forms.proForm()
    if request.method == "POST":
        form = forms.proForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
    return render(request,'apptwo/users.html',{'form':form})
