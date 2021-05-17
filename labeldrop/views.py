from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#Python Functions
def hello(request):
   text="""<h1> Label Validation </h1>"""
   return HttpResponse(text)

def display(request,id):
   text="LABEL VALIDATION JOB ID: %s"%id   
   return HttpResponse(text)