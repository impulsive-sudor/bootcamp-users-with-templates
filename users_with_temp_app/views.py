from django.shortcuts import render, redirect
from .models import users

def main(request):
    context = {
        'user': users.objects.get(id=1).__dict__,
        'test': "testme",
        'anuser': users.objects.all(),
    }
    return render(request, "main.html", context)

def form(request):
    if request.method == "POST":
        firstname = request.POST["first-name"]
        lastname = request.POST["last-name"]
        email = request.POST["email"]
        age = request.POST["age"]

        newuser = users(first_name=firstname, last_name=lastname, email=email, age=age)
        newuser.save()
        return redirect('/')

