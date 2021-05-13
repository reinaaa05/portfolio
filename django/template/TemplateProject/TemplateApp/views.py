from django.shortcuts import render

def index(request):
    val = 'GoodBay'
    return render(request,'index.html',context={'value':val})

def home(request):
    my_name = 'Taro Yamada'
    favourite_fruits = ['Apple','Grape','Lemon']
    my_info = {
        'name' : 'Taro',
        'age':18
    }
    status = 20
    return render(request,'home.html',context={
        'my_name' :my_name,
        'favourite_fruits':favourite_fruits,
        'my_info':my_info,
        'status': status
    })

def sample1(request):
    return render(request,'sample1.html')

def sample2(request):
    return render(request,'sample2.html')

