import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ModelProject.settings')
from django import setup
setup()

from ModelApp.models import Students,Person

# print(Students.objects.all())

# IN
ids = [13, 14, 15]
#print(Students.objects.filter(pk__in=ids).all())

# contain　部分一致
#print(Students.objects.filter(name__contains='三').all())

# p = Person(
#     first_name='Jiro',last_name='Yamada',
#     birthday='2000-01-01',email='aa@mail.com',
#     salary=1000,memo='memo taro',web_site=''
# )

# p.save()

# is null
# print(Person.objects.filter(salary__isnull=True).all())

#  レコードを取り除く
# print(Person.objects.exclude(salary__isnull=True).all())
# print(Students.objects.exclude(name='太郎').all())

#一部カラムを取り除く
# print(Students.objects.values('name','age').all().query)
# students = Students.objects.values('name','age','id').all()
# for student in students:
#     print(student['id'])

# 並び替え
print(Students.objects.order_by('name','-id').all())