from django.contrib import admin
from .models import TeacherFaceData,StudentFaceData
# Register your models here.


class StudentFaceDataAdmin(admin.ModelAdmin):
    list_display = ('stu_info','is_trained')
    list_filter = ('is_trained',)


class TeacherFaceDataAdmin(admin.ModelAdmin):
    list_display = ('teacher_info','is_trained')
    list_filter = ('is_trained',)


admin.site.register(TeacherFaceData,TeacherFaceDataAdmin)
admin.site.register(StudentFaceData,StudentFaceDataAdmin)