from django.shortcuts import render,redirect
from django.contrib.auth.models import User #already a default user model present on django
from django.contrib.auth import login,logout,authenticate

import csv
from django.http import HttpResponse

#fro popup messages
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,"index.html")
def regiser(request):
    if request.method=="POST":
    #fields for custom user
        username=request.POST['username']
        email=request.POST['Email']
        password=request.POST['password']
    #now we have to send this fields to User model
        user=User(username=username,email=email,password=password) #Invalid password format or unknown hashing algorithm
    #to solve above password->User.objects.create_user(parameters)
        # user=User.objects.create_user(username=username,email=email,password=password)
        user.save()

        #for popup messages
        #messages tags
# Debug | debug | debug
# Info | info | info
# Success | success | success
# Warning | warning | warning
# Error | error | error
        messages.success(request,'your have register successfully')
    #after saving you have to aagin home page
        return redirect('home') # this name="home" which we have given in urls.py from app
    return render(request,"register.html")


#for authentication means login

def login_user(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(username=username,password=password)
        if user is not  None:
            login(request,user)
            #user logic
            messages.success(request,"you have succesfully login....!")
            return redirect('home')
        else:
            messages.warning(request,"Invalid credentials found..")
            return render(request,"login.html")
    return render(request,"login.html")

def logout_user(request):
    # messages.success(request,"you have successfully logout..")

    logout(request)
    return redirect('home')


def download_csv(request):
    response=HttpResponse(content_type='text/csv') # Create an HttpResponse object with content type 'text/csv'
    response['Content-Dispotion']='attachment; filename="users.csv"'# # Set the Content-Disposition header to indicate a file attachment with a filename of 'users.csv'

    writer=csv.writer(response)# Create a CSV writer object
    writer.writerow(['Username','Email','password'])# Write the header row to the CSV file
    users=User.objects.all().values_list('username','email','password')# Fetch all users from the database and get their username, email, and password as a list of tuples
    print(users)
    for user in users:
        writer.writerow(user) # Write each user's data to the CSV file

    return response# Return the response object, which now contains the CSV data