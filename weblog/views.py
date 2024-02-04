from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to test website for Xcode academy ! This is the home page.")
