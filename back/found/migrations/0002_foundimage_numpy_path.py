# Generated by Django 3.0.5 on 2020-04-25 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('found', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='foundimage',
            name='numpy_path',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
