# Generated by Django 5.1.4 on 2025-02-25 07:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_alter_like_blog_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='blog_post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.blogpost'),
        ),
    ]
