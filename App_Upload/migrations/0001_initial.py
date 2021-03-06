# Generated by Django 3.1.5 on 2021-01-07 15:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=264)),
                ('video', models.FileField(upload_to='upload_video')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='upload_thumbnail')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='uploaded_video', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Unlike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unlike_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_unliked_video', to=settings.AUTH_USER_MODEL)),
                ('video_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unliked_video_post', to='App_Upload.videopost')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_liked_video', to=settings.AUTH_USER_MODEL)),
                ('video_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liked_video_post', to='App_Upload.videopost')),
            ],
        ),
    ]
