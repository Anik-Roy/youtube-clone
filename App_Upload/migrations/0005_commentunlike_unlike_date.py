# Generated by Django 3.1.5 on 2021-01-10 11:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('App_Upload', '0004_commentlike_commentunlike'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentunlike',
            name='unlike_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
