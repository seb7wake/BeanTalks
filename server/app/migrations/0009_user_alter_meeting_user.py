# Generated by Django 4.1.6 on 2023-06-17 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_meeting_user_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('email', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.AlterField(
            model_name='meeting',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meetings', to='app.user'),
        ),
    ]