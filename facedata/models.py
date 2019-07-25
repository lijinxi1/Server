from django.db import models
from register.models import Student,Teacher
# Create your models here.


class StudentFaceData(models.Model):
    is_trained=models.BooleanField(verbose_name='是否训练')
    stu_info=models.ForeignKey(Student,on_delete=models.CASCADE,verbose_name='学生')

    class Meta:
        verbose_name='学生人脸数据'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.stu_info.stu_name


class TeacherFaceData(models.Model):
    is_trained=models.BooleanField(verbose_name='是否训练')
    teacher_info=models.ForeignKey(Teacher,on_delete=models.CASCADE,verbose_name='教师')

    class Meta:
        verbose_name='教师人脸数据'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.teacher_info.teacher_name
