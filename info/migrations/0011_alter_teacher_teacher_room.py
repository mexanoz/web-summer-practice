# Generated by Django 4.0.6 on 2022-07-07 02:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0010_alter_lesson_lesson_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='teacher_room',
            field=models.OneToOneField(limit_choices_to={'room_type': 'TE'}, on_delete=django.db.models.deletion.RESTRICT, to='info.room'),
        ),
    ]
