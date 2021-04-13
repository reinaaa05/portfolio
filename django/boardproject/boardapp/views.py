from django.shortcuts import render
from django.contrib.auth.models import User

def signupfunc(request):
    object = User.objects.get(username='user01')
    print(object.email)
    if request.method == "POST":
        print('this is post method')
    else:
        print('this is not method')
    return render(request, 'signup.html', {'some':100})
