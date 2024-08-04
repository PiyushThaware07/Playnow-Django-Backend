# Generated by Django 5.0.7 on 2024-08-04 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_movie_created_by_alter_movie_updated_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='updated_by',
        ),
        migrations.AddField(
            model_name='movie',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
