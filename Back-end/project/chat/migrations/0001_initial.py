# Generated by Django 4.2.6 on 2023-10-22 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=30)),
                ('receiver', models.CharField(max_length=30)),
                ('sent_at', models.DateTimeField(auto_now_add=True)),
                ('content', models.CharField(max_length=500)),
            ],
        ),
    ]
