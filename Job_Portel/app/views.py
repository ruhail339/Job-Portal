from email import message
from django.shortcuts import render, redirect
from .models import UserMaster, Candidate, Company
from random import randint

from django.contrib.auth  import authenticate,  login, logout
# Create your views here.

# Index Page View function...///front page
def IndexPage(request):

    return render(request, "app/index.html")


# Signup page view function..
def SignUp(request):
    
    return render(request, "app/signup.html")

# User Register Page view function
def RegisterUser(request):
    
    # if request.method == "POST":
    if request.POST['role']=="Candidate":
            
        role = request.POST['role']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
    
        user = UserMaster.objects.filter(email=email)
            
            
        if user:
                
            message = "User already Exist"

            return render(request, "app/signup.html", {'msg1' : message})
        else:
                
            if password == cpassword:
                    
                otp = randint(100000, 999999)
                newuser = UserMaster.objects.create(role=role, otp=otp, email=email, password=password)
                newcand = Candidate.objects.create(user_id=newuser, firstname=fname, lastname=lname)
                
                return render(request, "app/otpverify.html", {'email' : email})
                
            else:
                    
                message = "Confirm password does not Match!"

                return render(request, "app/signup.html", {'msg2' : message})
                
    else:
            
        if request.POST['role']=="Company":
            
            role = request.POST['role']
            fname = request.POST['firstname']
            lname = request.POST['lastname']
            email = request.POST['email']
            password = request.POST['password']
            cpassword = request.POST['cpassword']
        
            user = UserMaster.objects.filter(email=email)
            
            if user:
                
                message = "Company already Exist"

                return render(request, "app/signup.html", {'msg1' : message})
    

            else:
                
                if password == cpassword:
                    
                    otp = randint(100000, 999999)
                    newuser = UserMaster.objects.create(role=role, otp=otp, email=email, password=password)
                    newcomp = Company.objects.create(user_id=newuser, firstname=fname, lastname=lname)
                    
                    return render(request, "app/otpverify.html", {'email' : email})

                else:
                    
                    message = "Confirm password does not Match!"

                    return render(request, "app/signup.html", {'msg2' : message})
                
# otppage view function

def OtpPage(request):
    
    return render(request, "app/otpverify.html")


# OTP Verification function
def OtpVerify(request):

    email = request.POST['email']
    otp = int(request.POST['otp'])

    user = UserMaster.objects.get(email=email)

    if user:
        if user.otp == otp:
            
            message = "OTP Verify successfully"
            return render(request, "app/login.html", {'msg' : message})
        
        else:
            
            message = "OTP is incorrect"
            
            return render(request, "app/otpverify.html", {'msg' : message, 'email' : email})
    
    else:
        
        return render(request, "app/signup.html")
    
    
    
# Login page view function

def Loginpage(request):
    
    return render(request, "app/login.html")


# create login function for user view
def LoginUser(request):
    if request.POST['role']=="Candidate":
        
        email = request.POST['email']
        password = request.POST['password']
        
        # checking the email id with database email id
        user = UserMaster.objects.get(email = email)
        
        if user:
            if user.password == password and user.role=="Candidate":
                
                can = Candidate.objects.get(user_id=user)

                request.session['id'] = user.id
                request.session['role'] = user.role
                request.session['firstname'] = can.firstname
                request.session['lastname'] = can.lastname
                request.session['email'] = user.email

                return redirect("index")
            
            else:
                
                message = "Password does not Match" 
                return render(request, "app/login.html", {'msg1' : message})

        else:
            
            message = "User does not exist"
            return render(request, "app/login.html", {"msg2" : message})
    
    else:
           
        if request.POST['role']=="Company":
            
            email = request.POST['email']
            password = request.POST['password']
            
            # checking the email id with database email id
            user = UserMaster.objects.get(email = email)
            
            if user:
                if user.password == password and user.role=="Company":
                    
                    com = Company.objects.get(user_id=user)

                    request.session['id'] = user.id
                    request.session['role'] = user.role
                    request.session['firstname'] = com.firstname
                    request.session['lastname'] = com.lastname
                    request.session['email'] = user.email

                    return redirect("index")
                
                else:
                    
                    message = "Password does not Match" 
                    return render(request, "app/login.html", {'msg1' : message})

            else:
                
                message = "User does not exist"
                return render(request, "app/login.html", {"msg2" : message})
            
        else:
            
            message = "Please select role"
            return render(request, "app/login.html", {'msg3' : message})
    




# Logout view function
def Logout(request):
    
    try:
        del request.session['email']

        message.success(request, "Succesfully Logged Out")
    
    except:
        
        return redirect("index")
    return redirect("index")
    




# User profile page view function 
def ProfilePage(request):
    
    return render(request, "app/profile.html")
    
    