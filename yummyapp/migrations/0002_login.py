# Generated by Django 5.0.2 on 2024-03-01 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yummyapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
