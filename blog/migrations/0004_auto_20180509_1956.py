# Generated by Django 2.0.4 on 2018-05-09 19:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180508_0452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authored_comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.Post'),
        ),
    ]
