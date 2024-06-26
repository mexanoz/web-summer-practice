# Generated by Django 4.0.6 on 2022-07-12 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0014_rename_discipline_groups_discipline_groups_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='lesson_type',
            field=models.CharField(choices=[('ЛК', 'лекции'), ('ПР', 'практики')], default='ПР', max_length=2),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='photo',
            field=models.ImageField(upload_to='photos'),
        ),
    ]
