# Generated by Django 5.1.4 on 2025-02-25 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_rename_user_comment_author_alter_comment_blog_post_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='author',
            new_name='user',
        ),
    ]
