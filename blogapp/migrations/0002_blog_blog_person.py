# Generated by Django 4.0 on 2021-12-15 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_person',
            field=models.TextField(null=True),
        ),
    ]
