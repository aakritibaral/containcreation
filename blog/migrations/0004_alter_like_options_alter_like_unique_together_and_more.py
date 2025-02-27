# Generated by Django 5.1.4 on 2025-02-24 05:19

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_comment_post_comment_blog_post'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='like',
            options={},
        ),
        migrations.AlterUniqueTogether(
            name='like',
            unique_together={('user', 'post')},
        ),
        migrations.AlterModelTable(
            name='like',
            table=None,
        ),
    ]
