from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to the first app!")

def index1(request):
    return HttpResponse("varu!")

