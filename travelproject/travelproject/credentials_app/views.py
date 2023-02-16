from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.

# user registration function
def register(request):
    if request.method == 'POST': # fetching details from database
        urna = request.POST['username']
        fna = request.POST['first_name']
        lna = request.POST['last_name']
        mail = request.POST['email']
        pswd = request.POST['password']
        cpswd = request.POST['password1']
        if pswd == cpswd: # to check whether the given password is equal to the confirmation password
            if User.objects.filter(username = urna).exists(): # to check if username and email already taken
                messages.info(request,"Username already taken")
                return redirect('register')
            elif User.objects.filter(email = mail).exists():
                messages.info(request,"Email already taken")
                return redirect('register')
            else: # if username and email not taken new user created
                user = User.objects.create_user(username = urna,first_name = fna,last_name = lna,email = mail,password = pswd)
                user.save();
                return redirect('login')
        else: # or else redirected to register page
            messages.info(request,"Password not matching")
            return redirect('register')
        return redirect('/') # or redirected to home page
    return render(request,"register.html")

# user login function
def login(request):
    if request.method == 'POST': # fetching details from database
        urna = request.POST['usernam']
        pswd = request.POST['passwor']
        user = auth.authenticate(username = urna,password = pswd) # checking with the auth table
        if user is not None: # if user is in auth table
            auth.login(request,user)
            return redirect('/')
        else: # else redirected to login page
            messages.info(request,"Invalid Entry")
            return redirect('login')
    return render(request,"login.html")

# user logout function
def logout(request):
    auth.logout(request)
    return redirect('/')

