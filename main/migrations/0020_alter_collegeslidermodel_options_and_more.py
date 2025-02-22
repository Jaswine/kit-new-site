# Generated by Django 4.2.7 on 2023-12-23 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_collegeslidermodel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='collegeslidermodel',
            options={'verbose_name': 'Слайдер на главной странице', 'verbose_name_plural': 'Слайдер на главной странице'},
        ),
        migrations.AddField(
            model_name='collegeslidermodel',
            name='image2',
            field=models.ImageField(blank=True, upload_to='uploads/slider', verbose_name='Изображение 2'),
        ),
        migrations.AddField(
            model_name='collegeslidermodel',
            name='image3',
            field=models.ImageField(blank=True, upload_to='uploads/slider', verbose_name='Изображение 3'),
        ),
    ]
