# Generated by Django 4.2.7 on 2023-11-13 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Task name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Task description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date of creation')),
                ('due_date', models.DateTimeField(blank=True, null=True, verbose_name='Deadline')),
                ('completed', models.BooleanField(default=False, verbose_name='The task is completed')),
            ],
        ),
    ]
