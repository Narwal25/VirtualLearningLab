# Generated by Django 3.0.5 on 2020-06-12 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0011_auto_20200612_1143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='body',
        ),
        migrations.RemoveField(
            model_name='post',
            name='course_id',
        ),
    ]