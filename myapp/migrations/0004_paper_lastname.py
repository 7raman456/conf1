# Generated by Django 4.1 on 2022-08-21 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_paper'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='lastname',
            field=models.CharField(default='SOME STRING', max_length=200),
        ),
    ]
