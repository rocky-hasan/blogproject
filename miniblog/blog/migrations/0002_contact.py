# Generated by Django 4.1.7 on 2023-04-16 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('message', models.TextField()),
            ],
        ),
    ]
