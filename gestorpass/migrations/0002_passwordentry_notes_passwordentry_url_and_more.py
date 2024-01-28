# Generated by Django 5.0.1 on 2024-01-27 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestorpass', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='passwordentry',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='passwordentry',
            name='url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='passwordentry',
            name='password',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='passwordentry',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='passwordentry',
            name='username',
            field=models.CharField(max_length=255),
        ),
    ]
