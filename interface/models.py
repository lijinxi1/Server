from django.db import models
# Create your models here.


from register.models import Student,Teacher

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




