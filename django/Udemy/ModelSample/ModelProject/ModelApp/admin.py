from django.contrib import admin
from .models import Person, Prefectures, Students

admin.site.register(Person)
admin.site.register(Students)
admin.site.register(Prefectures)


