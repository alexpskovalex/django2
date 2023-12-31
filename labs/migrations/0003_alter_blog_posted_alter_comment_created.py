# Generated by Django 4.2.6 on 2023-12-26 05:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0002_blog_image_alter_blog_posted_alter_comment_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2023, 12, 26, 8, 25, 58, 816991), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2023, 12, 26, 8, 25, 58, 816991), verbose_name='Опубликована'),
        ),
    ]
