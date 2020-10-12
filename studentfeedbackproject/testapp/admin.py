from django.contrib import admin
from testapp.models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=['name','rollno','email','password','rpassword','feedback']

admin.site.register(Student,StudentAdmin)
