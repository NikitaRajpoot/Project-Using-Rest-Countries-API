from django.shortcuts import render
from django.http import HttpResponse

def first(request):
    return HttpResponse("<h1 style='color:green';>First Django Page is created</h1>")

def index(request):
    str="I am from Views File"
    data = ["red","green","blue","Magenta"]
    context={"colors":data,"string":str}
    return render(request,"index.html",context) 

def Countries(request):
    return render(request,"countries.html")    