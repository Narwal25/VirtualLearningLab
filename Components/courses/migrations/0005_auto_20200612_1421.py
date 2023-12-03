# Generated by Django 3.0.5 on 2020-06-12 21:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_auto_20200612_1414'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='completion',
        ),
        migrations.AlterField(
            model_name='courses',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]