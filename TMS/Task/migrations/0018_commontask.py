# Generated by Django 4.2.7 on 2023-12-02 08:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Task', '0017_delete_commontask'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommonTask',
            fields=[
                ('task_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Task.task')),
                ('shared_with', models.ManyToManyField(related_name='tasks_participated', to=settings.AUTH_USER_MODEL)),
            ],
            bases=('Task.task',),
        ),
    ]
