from django.shortcuts import render , HttpResponse , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def profile(request):
    return render(request, 'member/profile.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        secondname = request.POST['secondname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if(pass1==pass2):
            myuser = User.objects.create_user(username, email, pass1)
            myuser.first_name = firstname
            myuser.last_name = secondname
            myuser.save()
        return redirect('profile')

    return render(request, 'member/register.html')

def handleLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username , password = password)
        if user is not None:
            login(request,user)
            return redirect('popular')
        
        else:
            return HttpResponse('404 Not found')
    
    render(request,'food/profile.html')


def handleLogout(request):
    logout(request)
    return redirect('index')