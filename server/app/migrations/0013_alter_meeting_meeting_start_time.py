# Generated by Django 4.1.6 on 2023-07-09 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_rename_invitee_additional_info_meeting_invitee_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='meeting_start_time',
            field=models.DateTimeField(default='2023-06-09 21:00:00'),
            preserve_default=False,
        ),
    ]
