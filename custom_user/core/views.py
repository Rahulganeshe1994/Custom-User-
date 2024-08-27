from django.shortcuts import render,redirect
from .forms import RegisterForm ,UpdateProfileForm,UserPasswordChangeForm
from django.contrib import messages
from django.contrib.auth import authenticate ,login,logout

# Create your views here.


def signup(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Account Created Successfully")
            return redirect('profile')
    context = {'form':form}
    return render(request,'core/signup.html',context)


def signin(request):
    if request.method =='POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request,email=email,password=password)
        if user is not None:
            login(request,user)
            return redirect('profile')
        else:
            messages.warning(request,"Invalid Credentials")
            return redirect('signin')
    context = {}
    return render(request,'core/signin.html',context)


def signout(request):
    logout(request)
    return redirect('signin')

def profile(request):
    user = request.user
    context = {'user':user}
    return render(request,'core/profile.html',context)

def update_profile(request):
    if request.user.is_authenticated:
        user = request.user
        form = UpdateProfileForm(instance=user)
        if request.method == "POST":
            form = UpdateProfileForm(request.POST,request.FILES,instance=user)
            if form.is_valid():
                form.save()
                messages.success(request,"Profile Update Successfully")
                return redirect('profile')
    context = {'form':form}
    return render(request ,'core/update_profile.html',context)


