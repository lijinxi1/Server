# Generated by Django 2.2.3 on 2019-07-25 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0002_auto_20190725_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='stu_sign_status',
            field=models.BooleanField(verbose_name='签到状态'),
        ),
    ]
