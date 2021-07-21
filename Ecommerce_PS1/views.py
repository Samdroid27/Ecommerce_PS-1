from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

def index(request):
    return render(request, 'index.html')



def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        inputPassword = request.POST['logininputPassword']
        user = authenticate(username=loginusername,password=inputPassword)
        if user is not None :
            login(request,user)
            return redirect('/shop')
        else:
            messages.error(request,"Invalid credentials")
            return redirect('/')

def handleLogout(request):
    logout(request)
    return redirect('/')

def handleSignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['inputEmail']
        inputPassword = request.POST['inputPassword']
        confirmInputPassword = request.POST['confirmInputPassword']

        #Check
        if len(username) > 10:
            messages.error(request, "username must be under 10 characters")
            return redirect("/")
        if inputPassword != confirmInputPassword :
            messages.error(request, "PassWords do not match")
            return redirect("/")
        #Create User
        myuser = User.objects.create_user(username,email,inputPassword)
        myuser.first_name = fname
        myuser.last_name = lname 
        myuser.save()
        messages.success(request,"Your user created successfully")
        return redirect('/')
    else:
        return HttpResponse('404 - Not Found') 