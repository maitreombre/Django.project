# Generated by Django 4.2.7 on 2023-11-16 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0006_alter_priority_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priority',
            name='value',
            field=models.CharField(choices=[(1, 'Default'), (2, 'Low'), (3, 'Medium'), (4, 'High')], default='1', max_length=10, verbose_name='Priority value'),
        ),
    ]
