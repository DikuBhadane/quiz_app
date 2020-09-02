from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from .forms import QuizForm
# Create your views here.

def name(request):
    if request.method == "POST":
        return redirect('cricketer')
    return render(request, 'Name.html',{})

def cricketer(request):
    if request.method == "POST":
        return redirect('flag')
    return render(request, 'cricketer.html',{})

def flag(request):
    if request.method == "POST":
        return redirect('quiz')
        # return HttpResponseRedirect('name')
    return render(request, 'flag.html',{})