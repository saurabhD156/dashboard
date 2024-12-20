# Generated by Django 5.1.4 on 2024-12-07 14:50

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
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_image', models.ImageField(max_length=2000, upload_to='images/')),
                ('medium_image', models.ImageField(max_length=900, upload_to='images/')),
                ('small_image', models.ImageField(max_length=300, upload_to='images/')),
                ('alt_tag', models.CharField(blank=True, max_length=250, null=True)),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('description', models.TextField(blank=True, max_length=250, null=True)),
                ('fileName', models.CharField(blank=True, max_length=250, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='MetaData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=250)),
                ('description', models.TextField(max_length=250)),
                ('keywords', models.CharField(max_length=250)),
                ('index', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('featured_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.image')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250)),
                ('description', models.TextField(max_length=250)),
                ('slug', models.SlugField(unique=True)),
                ('images', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.image')),
                ('metadata', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.metadata')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField(unique=True)),
                ('metadata', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.metadata')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('short_description', models.TextField(max_length=250)),
                ('content', models.TextField()),
                ('comments', models.TextField(max_length=500)),
                ('views', models.PositiveIntegerField()),
                ('slug', models.SlugField(unique=True)),
                ('published', models.BooleanField(default=False)),
                ('category', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='core.category')),
                ('featured_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.image')),
                ('metadata', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='core.metadata')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(blank=True, related_name='posts', to='core.tag')),
            ],
        ),
    ]
