# Generated by Django 3.2.18 on 2023-03-26 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deck',
            name='last_revised',
            field=models.DateTimeField(),
        ),
    ]
