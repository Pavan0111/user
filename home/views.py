from django.shortcuts import render, HttpResponse, redirect

from django.contrib import messages
from django.contrib.auth  import authenticate,  login, logout
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def post(request):
    return render(request, 'post/post.html')  

def product(request):
    return render(request, 'product/product.html')


def handleSignup(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
        if len(username)>10:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('home')
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('home')
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your Portal has been successfully created")
        return redirect('home')

    else:
        return HttpResponse("404 - Not found")

def handlelogin(request):
     if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")
     return HttpResponse('handlelogin')
     return HttpResponse("404 - Not found")

def handlelogout(request):
       logout(request)
       messages.success(request,"successfully logged out")
       return redirect('home')
       return HttpResponse('handlelogout')