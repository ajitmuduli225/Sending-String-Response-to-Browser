from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.





def ajit(request):
    return HttpResponse('<h1>Hey, This Is Ajit</h1>')


def rohit(request):
    return HttpResponse('<h1><marquee>One Of The Best captain in Current Indian Team<marquee></h1>')


def bumrah(request):
    return HttpResponse('He Is The Best Bowler That Indian Team Has!!')
