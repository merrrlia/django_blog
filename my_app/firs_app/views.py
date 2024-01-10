from django.shortcuts import render

def index(request):
    return render(request, 'firs_app/index.html')

def about(request):
    return render(request, 'firs_app/about.html') 