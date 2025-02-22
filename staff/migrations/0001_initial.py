# Generated by Django 4.2.7 on 2023-12-19 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CMCModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('title_ru', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('title_kk', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('title_en', models.CharField(max_length=255, null=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'ЦМК дисциплины и другие',
                'verbose_name_plural': 'ЦМК дисциплины и другие',
            },
        ),
        migrations.CreateModel(
            name='PositionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('title_ru', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('title_kk', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('title_en', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('cmc', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='staff.cmcmodel')),
            ],
            options={
                'verbose_name': 'Справочник должностей',
                'verbose_name_plural': 'Справочник должностей',
            },
        ),
        migrations.CreateModel(
            name='PersonModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=100, verbose_name='ФИО')),
                ('fio_ru', models.CharField(max_length=100, null=True, verbose_name='ФИО')),
                ('fio_kk', models.CharField(max_length=100, null=True, verbose_name='ФИО')),
                ('fio_en', models.CharField(max_length=100, null=True, verbose_name='ФИО')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
                ('foto', models.ImageField(blank=True, upload_to='upload/about-college/staff', verbose_name='Фото')),
                ('info', models.TextField(blank=True, verbose_name='Информация')),
                ('info_ru', models.TextField(blank=True, null=True, verbose_name='Информация')),
                ('info_kk', models.TextField(blank=True, null=True, verbose_name='Информация')),
                ('info_en', models.TextField(blank=True, null=True, verbose_name='Информация')),
                ('is_working', models.BooleanField(default=False, verbose_name='Статус работы')),
                ('cmc', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='staff.cmcmodel', verbose_name='ЦМК')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='staff.positionmodel', verbose_name='Должность')),
            ],
            options={
                'verbose_name': 'Персонал',
                'verbose_name_plural': 'Персонал',
            },
        ),
        migrations.CreateModel(
            name='GroupModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название группы')),
                ('name_ru', models.CharField(max_length=150, null=True, verbose_name='Название группы')),
                ('name_kk', models.CharField(max_length=150, null=True, verbose_name='Название группы')),
                ('name_en', models.CharField(max_length=150, null=True, verbose_name='Название группы')),
                ('curator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='staff.personmodel', verbose_name='Куратор группы')),
            ],
            options={
                'verbose_name': 'Группа',
                'verbose_name_plural': 'Группа',
            },
        ),
    ]
