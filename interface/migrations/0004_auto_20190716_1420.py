# Generated by Django 2.2.3 on 2019-07-16 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0003_auto_20190714_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='stu_sign_time',
            field=models.DateTimeField(auto_now=True, verbose_name='签到时间'),
        ),
        migrations.CreateModel(
            name='TeacherFaceData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_trained', models.BooleanField(verbose_name='是否训练')),
                ('teacher_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interface.Teacher')),
            ],
            options={
                'verbose_name': '教师人脸数据',
                'verbose_name_plural': '教师人脸数据',
            },
        ),
        migrations.CreateModel(
            name='StudentFaceData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_trained', models.BooleanField(verbose_name='是否训练')),
                ('stu_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interface.Student')),
            ],
            options={
                'verbose_name': '学生人脸数据',
                'verbose_name_plural': '学生人脸数据',
            },
        ),
    ]