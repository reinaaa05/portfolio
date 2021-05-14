from django.http import request
from django.shortcuts import render

class Member:
    def __init__(self, id, name,join_at,picture_path):
        self.id = id
        self.name = name
        self.join_at = join_at
        self.picture_path = picture_path

member_list = [
    Menber(0, 'Taro','2018/04/01,'img/taro.jpg'),
    Menber(1, 'Jiro','2019/04/01,'img/jiro.jpg'),
    Menber(2, 'Hanako','2019/05/01,'img/hanako.jpg'),
    Menber(3, 'Yoshiko','2018/10/01,'img/yoshiko.jpg'),
]


#ホーム画面
def home(request):
    return render(request,'home.html')

#メンバー一覧画面
def menbers(request):
    return render(request,'members.html',context={
        'members':member_list
    })

#メンバーの画面詳細
def member(request,id):
    return render(request,'member_detail.html',context={
        'member':member_list[id]
    })