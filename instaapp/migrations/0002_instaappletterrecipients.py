# Generated by Django 3.1.3 on 2020-11-23 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instaapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstaAppLetterRecipients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
