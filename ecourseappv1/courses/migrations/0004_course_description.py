# Generated by Django 5.0.3 on 2024-03-05 08:20

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_course_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='description',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
