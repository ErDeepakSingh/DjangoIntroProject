from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def users_list(request):
    #return HttpResponse("Hello")
    return render(request, 'users/index.html')

def login(request):

    return render(request, 'users/loginform.html')
