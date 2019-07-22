from django.contrib import admin
from .models import Teacher,Student,Course
# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ('stu_id','stu_name','stu_class')
    list_filter = ('stu_class',)


class TeacherAdmin(admin.ModelAdmin):
    list_display= ('teacher_id','teacher_name')


class CourseAdmin(admin.ModelAdmin):
    list_display = ('stu_info','stu_sign_status','stu_sign_time','course','teacher_info','classroom')
    list_filter = ('course','classroom','teacher_info')


admin.site.register(Teacher,TeacherAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Course,CourseAdmin)
