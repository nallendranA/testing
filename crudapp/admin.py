from django.contrib import admin
from crudapp.models import Student
class StudentAdmin(admin.ModelAdmin):
    list_display=['sno','name','age','dep']
admin.site.register(Student,StudentAdmin)

# Register your models here.
