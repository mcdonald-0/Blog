# Generated by Django 3.2.4 on 2021-07-16 02:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210716_0333'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='date_jadded',
            new_name='date_added',
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.userprofile'),
        ),
    ]
