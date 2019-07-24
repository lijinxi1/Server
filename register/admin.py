from django.contrib import admin
from .models import *
# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ('stu_id','stu_name','stu_class')
    list_filter = ('stu_class',)


class TeacherAdmin(admin.ModelAdmin):
    list_display= ('teacher_id','teacher_name')


admin.site.register(Teacher,TeacherAdmin)
admin.site.register(Student,StudentAdmin)