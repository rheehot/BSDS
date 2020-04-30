# Generated by Django 3.0.5 on 2020-04-28 15:06

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import imagekit.models.fields
import lost.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('found', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LostImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=lost.models.lost_image_path)),
                ('category_1', models.CharField(blank=True, max_length=20)),
                ('category_2', models.CharField(blank=True, max_length=20)),
                ('category_3', models.CharField(blank=True, max_length=20)),
                ('numpy_path', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='LostPosting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('status', models.BooleanField(blank=True)),
                ('content', models.TextField(blank=True)),
                ('lostname', models.CharField(blank=True, max_length=100)),
                ('password', models.CharField(blank=True, max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('do_notice', models.BooleanField()),
                ('lost_time', models.DateTimeField()),
                ('x', models.CharField(blank=True, max_length=50, null=True)),
                ('y', models.CharField(blank=True, max_length=50, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='found.Category')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='found.Color')),
            ],
            options={
                'ordering': ('-lost_time',),
            },
        ),
        migrations.CreateModel(
            name='LostThumbnail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to=lost.models.lost_thumbnail_path)),
                ('origin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thumbnail', to='lost.LostImage')),
                ('posting', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thumbnail', to='lost.LostPosting')),
            ],
        ),
    ]