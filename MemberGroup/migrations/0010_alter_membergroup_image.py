# Generated by Django 3.2.4 on 2021-08-07 03:25

import MemberGroup.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MemberGroup', '0009_alter_membergroup_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membergroup',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to=MemberGroup.models.UploadSrcImageInfo),
        ),
    ]
