from django.shortcuts import render
from django.http import HttpResponse
#it handel as the middleware
import random

# Create your views here.

#def home(request):
#   return HttpResponse('Hello there !! ,this is root URL same app')
"""
def menu(request):
    return HttpResponse("This is other URL inside the same app")

"""

def home(request):
    return render(request,'generator/home.html',{'password':'dumbleDoor'})

def about(request):
    return render(request,'generator/about.html')

def password(request):
    thepassword='testing'
    characters=list('abcdefghijklmnopqrstuvwxyz')
    
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    
     
    if request.GET.get('number'):
        characters.extend(list('0123456789'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*'))    

    lenght=int(request.GET.get('length'))

    thepassword=''

    for i in range(lenght):
        thepassword+=random.choice(characters)

    return render(request,"generator/password.html",{'password':thepassword})
