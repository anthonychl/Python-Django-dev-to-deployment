from django.shortcuts import render, redirect
from django.contrib import messages, auth  # importing 'messages' for our alerts. And 'auth' for logging 
from django.contrib.auth.models import User # the User model comes with django, we only need import it
from listings.models import Listing
from contacts.models import Contact

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)
        if user is not None: # if the user is found
            auth.login( request, user )
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST': # the form is submitted
        #register user
        first_name = request.POST['first_name'] # get the value from the form, where the input tag is of name = 'first_name'
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            #check user name
            if User.objects.filter(username = username).exists():
                messages.error(request,'Username taken')   
                return redirect('register')
            else:
                # check email
                if User.objects.filter(email = email).exists():
                    messages.error(request,'That email is being used')   
                    return redirect('register')
                else:
                    # OK
                    user = User.objects.create_user(first_name = first_name, last_name = last_name, username = username, email = email, password = password)

                    ## login automatically after register
                    #auth.login( request, user )
                    #messages.success(request, 'You are now logged in')
                    #return redirect('index')

                    ## registering the user and asking to log in manually
                    user.save()
                    messages.success(request, 'You are now registered')
                    return redirect('login')
        else:
            messages.error(request,'Passwords dont match')   
            return redirect('register')                     
    else:
        return render(request, 'accounts/register.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,"You are now logged out")
        return redirect('index')

def dashboard(request):
    if request.user.is_authenticated:
        contacts = Contact.objects.order_by('-contact_date').filter( user_id = request.user.id)
        context = {
            'contacts': contacts
        }
        return render(request, 'accounts/dashboard.html', context)

