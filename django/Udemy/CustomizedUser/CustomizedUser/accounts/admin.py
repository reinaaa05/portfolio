from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .forms import UserChangeForm, UserCreationForm

User = get_user_model()

class CustomizeUserAdmin(UserAdmin):
    form = UserChangeForm #ユーザー編集画面でつかう
    add_form = UserCreationForm #ユーザー作成画面
    list_display = ('username', 'email', 'is_staff') #一覧画面で表示する
    fieldsets = (
        ('ユーザー情報', {'fields':('username', 'email', 'password', 'website', 'picture')}),
        ('パーミッション', {'fields':('is_staff', 'is_active', 'is_superuser')}),
        )
    #ユーザー編集画面で表示する要素

    add_fieldsets = (
        (' ユーザー情報', {
            'fields': ('username', 'email', 'password', 'confirm_password')
        }),
    )

admin.site.register(User, CustomizeUserAdmin)