# Generated by Django 4.2.6 on 2023-10-30 22:14

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0008_remove_customuser_user_uuid"),
    ]

    operations = [
        migrations.CreateModel(
            name="FrindShip",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="customuser",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="userprofile",
            name="bio",
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="friends",
            field=models.ManyToManyField(
                blank=True, related_name="frinds", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
