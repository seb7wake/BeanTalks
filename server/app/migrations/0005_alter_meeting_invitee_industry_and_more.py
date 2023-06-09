# Generated by Django 4.1.6 on 2023-04-11 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_meeting_invitee_industry_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='invitee_industry',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='invitee_linkedin_url',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='invitee_name',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='meeting_link',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='meeting_notes',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='questions',
            field=models.TextField(blank=True, default=''),
        ),
    ]
