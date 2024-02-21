from django.shortcuts import render
from  django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request,"test.html" )
def news(request):
    return render(request,"news.html")
def events(request):
    return render(request,"events_oracle.html")
def oracle(request):
    return render(request,"events_oracle.html")