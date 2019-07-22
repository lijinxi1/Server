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


class Course(models.Model):
    stu_info = models.ForeignKey(Student, on_delete=models.CASCADE)
    stu_sign_time = models.DateTimeField(auto_now=True,verbose_name='签到时间')
    stu_sign_status = models.CharField(max_length=10, verbose_name='签到状态')

    course = models.CharField(max_length=50, verbose_name='课程名称')
    classroom = models.CharField(max_length=50, verbose_name='教室')

    teacher_info = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    class Meta:
        verbose_name = '课程签到情况'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.course


class StudentFaceData(models.Model):
    is_trained=models.BooleanField(verbose_name='是否训练')
    stu_info=models.ForeignKey(Student,on_delete=models.CASCADE)

    class Meta:
        verbose_name='学生人脸数据'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.stu_info


class TeacherFaceData(models.Model):
    is_trained=models.BooleanField(verbose_name='是否训练')
    teacher_info=models.ForeignKey(Teacher,on_delete=models.CASCADE)

    class Meta:
        verbose_name='教师人脸数据'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.teacher_info




