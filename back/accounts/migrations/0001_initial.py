# Generated by Django 3.0.5 on 2020-04-28 15:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=20, unique=True)),
                ('parent_department', models.CharField(max_length=30)),
                ('role', models.CharField(max_length=20)),
                ('center_name', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=30)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_name', models.CharField(max_length=200)),
                ('region_1depth_name', models.CharField(max_length=50)),
                ('region_2depth_name', models.CharField(max_length=50)),
                ('region_3depth_name', models.CharField(max_length=50)),
                ('road_name', models.CharField(max_length=50)),
                ('zone_no', models.CharField(max_length=20)),
                ('x', models.CharField(max_length=50)),
                ('y', models.CharField(max_length=50)),
                ('center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
