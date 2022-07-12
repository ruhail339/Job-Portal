
from django.urls import path
from app import views


urlpatterns = [

    path("", views.IndexPage, name="index"),
    path("signup/", views.SignUp, name="signup"),
    path("register/", views.RegisterUser, name="register"),
    
    path("otppage/", views.OtpPage, name="otppage"),
    path("otp/", views.OtpVerify, name="otp"),
    
    path("loginpage/", views.Loginpage, name="loginpage"),
    path("loginuser/", views.LoginUser, name="login"),
    path("logout/", views.Logout, name="logout"),
  
    path("profilepage/", views.ProfilePage, name="profilepage"),
    
]
 
