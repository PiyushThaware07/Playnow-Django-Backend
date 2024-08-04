# Generated by Django 5.0.7 on 2024-08-04 09:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_remove_movie_updated_by_movie_updated_by'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='updated_by',
        ),
        migrations.AddField(
            model_name='movie',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_movies', to=settings.AUTH_USER_MODEL),
        ),
    ]