# Generated by Django 4.2.2 on 2023-09-25 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_remove_callpairschedulemodel_pair_schedule_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studenteventmodel',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
    ]
