# Generated by Django 3.2.4 on 2021-07-18 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_blogpost_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='related_image',
            field=models.ImageField(default='defaultimg.jpg', null=True, upload_to=''),
        ),
    ]
