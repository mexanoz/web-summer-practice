# Generated by Django 4.0.6 on 2022-07-07 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0011_alter_teacher_teacher_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='teacher_education',
            field=models.CharField(max_length=20),
        ),
    ]
