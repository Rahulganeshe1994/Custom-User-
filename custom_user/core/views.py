from django.shortcuts import render

# Create your views here.


def signup(request):
    context = {}
    return render(request,'core/signup.html',context)