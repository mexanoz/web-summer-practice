# Generated by Django 4.0.6 on 2022-07-13 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0017_education_position_remove_discipline_groups_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]