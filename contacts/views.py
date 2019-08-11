from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.
def contact(request):
    if request.method == 'POST':
        #capture the form fields  
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        phone = request.POST['phone']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # create object
        contact = Contact(listing = listing, listing_id = listing_id, name = name, email = email,
                            phone = phone, message = message, user_id = user_id)
        
        # check for previous inquiry from the user (if logged in) about that property
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(user_id = user_id, listing_id = listing_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry on this listing')
                return redirect('/listings/'+listing_id)

        # save it to the DB
        contact.save()

        '''
        I commented all this because I dont want to leave my email here
        or set a dummy email right now :)
        but it works 
        Im using 'username@gmail.com' as a placeholder in this example

        # send email to realtor
        send_mail(
            'Property Inquiry: '+listing, # email subject
            "There's been an inquiry for "+ listing +" Check admin panel for more info", # email body
            'username@gmail.com', # the 'from' address, the one we set on our smtp in settings.py
            [realtor_email,'another@gmail.com'], # 'to', it can be one or more emails
            fail_silently= False # False for development
        )

        '''
        # send success message
        messages.success(request, 'Your inquiry has been sent, a realtor will get in touch with you soon')

        #this way of redirecting works
        #return redirect('listing', listing_id = listing_id) # this calls the view and passes the argument

        #this is how redirecting was done on the tutorial
        return redirect('/listings/'+listing_id) #  this just 'passes' the url to go to, another example of this could be: return redirect('https://example.com/')
