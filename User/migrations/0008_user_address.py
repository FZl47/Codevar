# Generated by Django 3.2.4 on 2021-08-02 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0007_user_phonenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Address',
            field=models.TextField(blank=True, null=True),
        ),
    ]
