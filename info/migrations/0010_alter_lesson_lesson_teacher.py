# Generated by Django 4.0.6 on 2022-07-07 02:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0009_remove_lesson_lesson_hours_a_week'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='lesson_teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='info.teacher'),
        ),
    ]
