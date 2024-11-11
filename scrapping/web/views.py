from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login 
from django.contrib.auth import logout as auth_logout
def login(request):
    if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            # Authenticate the user
            login_user = authenticate(request, username=username, password=password)

            if login_user is not None:
                auth_login(request, login_user)
                print("Logined....")
                return redirect('dashboard')  # Use redirect to the dashboard URL
            else:
                print("Incorrect username or password")
                return render(request, 'login.html', {'error_message': "Username and password do not match. Please try again!"})

    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if all([username, email, password]):
            try:
                # Create the User
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                print("user created successfully.....")
                return render(request, 'login.html',{'success_message':"User Added Successfull Please Log In Now..!"})
            except Exception as e:
                return render(request,'login.html',{'error_message':" Try agin to signup..."})
    return render(request,'signup.html')

def dash(request):
    return render(request,'dashboard.html')


def profile(request):
    return render(request,'profile.html')

def influencers_dash(request):
    return render(request,'influencers.html')


def influ_view(request):
    return render(request,'influencerProfile.html')

def influ_view01(request):
    return render(request,'profile01.html')

def faqs(request):
    return render(request,'faq.html')

def logout(request):
    auth_logout(request)
    return redirect('login')

def filter_popup(request):
    return render(request,'filter.html')

def forgot(request):
    return render(request,'forgot.html')



def privacy_policy(request):
    return render(request,'privacy.html')