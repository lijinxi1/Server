from django.contrib import admin
from .models import Teacher,Student,Course
# Register your models here.




class CourseAdmin(admin.ModelAdmin):
    list_display = ('stu_info','stu_sign_status','stu_sign_time','course','teacher_info','classroom')
    list_filter = ('course','classroom','teacher_info')



admin.site.register(Course,CourseAdmin)
