# Generated by Django 4.1 on 2022-08-21 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_contactus_delete_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='paper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paperid', models.CharField(max_length=200)),
                ('firstname', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('company', models.CharField(max_length=200)),
                ('jobtitle', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('Industry', models.CharField(max_length=200)),
                ('Intrests', models.TextField()),
            ],
        ),
    ]
