from django.shortcuts import render
from django.contrib.auth.models import User
from django.db import IntegrityError

def signupfunc(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, '', password)
            return render(request, 'signup.html', {'some':100})
        except IntegrityError:
            return render(request, 'signup.html', {'error':'このユーザーは既に登録されています登録されています'})
    return render(request, 'signup.html', {'some':100})
