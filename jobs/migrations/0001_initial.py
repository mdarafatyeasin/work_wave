# Generated by Django 5.0 on 2024-02-25 13:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='jobCategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=30)),
                ('slug', models.SlugField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='jobCircularModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('requirements', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=100)),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('last_date', models.DateTimeField()),
                ('vacancy', models.IntegerField()),
                ('salary', models.IntegerField()),
                ('job_category', models.ManyToManyField(to='jobs.jobcategorymodel')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]