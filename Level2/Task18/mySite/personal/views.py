from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "index.html")


# Store view
def store(request):
    return render(request, "store.html")


# Hello view
def hello(request):
    return render(request, "hello.html")
