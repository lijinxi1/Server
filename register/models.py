from django.db import models

# Create your models here.


class Student(models.Model):
    stu_id = models.CharField(max_length=20, verbose_name='学号')
    stu_name = models.CharField(max_length=50, verbose_name='姓名')
    stu_class = models.CharField(max_length=50, verbose_name='班级')
    stu_email = models.EmailField(verbose_name='邮箱')
    stu_phone = models.CharField(max_length=20, verbose_name='电话')
    stu_addr = models.CharField(max_length=50, verbose_name='地址')

    class Meta:
        verbose_name = '学生'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.stu_name


class Teacher(models.Model):
    teacher_id = models.CharField(max_length=20, verbose_name='工号')
    teacher_name = models.CharField(max_length=50, verbose_name='姓名')
    teacher_office = models.CharField(max_length=20, verbose_name='办公室')
    teacher_email = models.EmailField(verbose_name='邮箱')
    teacher_phone = models.CharField(max_length=20, verbose_name='电话')
    teacher_addr = models.CharField(max_length=50, verbose_name='地址')

    class Meta:
        verbose_name = '教师'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.teacher_name
