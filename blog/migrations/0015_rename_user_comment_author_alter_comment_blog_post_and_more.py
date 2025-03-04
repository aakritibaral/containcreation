# Generated by Django 5.1.4 on 2025-02-25 08:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_alter_like_blog_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user',
            new_name='author',
        ),
        migrations.AlterField(
            model_name='comment',
            name='blog_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.blogpost'),
        ),
        migrations.AlterField(
            model_name='like',
            name='blog_post',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='post_likes', to='blog.blogpost'),
            preserve_default=False,
        ),
    ]
