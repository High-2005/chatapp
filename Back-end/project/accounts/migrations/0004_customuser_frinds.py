# Generated by Django 4.2.6 on 2023-10-22 13:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_customuser_user_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='frinds',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
