# Generated by Django 3.0.5 on 2020-11-23 18:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('english_name', models.CharField(blank=True, max_length=1000, null=True)),
                ('native_name', models.CharField(blank=True, max_length=1000, null=True)),
                ('code', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50)),
                ('text', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=1000, null=True)),
                ('description', models.TextField()),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(null=True, upload_to='')),
                ('bio', models.TextField(blank=True, null=True)),
                ('fluent_languages', models.ManyToManyField(related_name='fluent_users', to='app.Language')),
                ('followers', models.ManyToManyField(blank=True, related_name='following', to=settings.AUTH_USER_MODEL)),
                ('following', models.ManyToManyField(blank=True, related_name='followed_by', to=settings.AUTH_USER_MODEL)),
                ('learning_languages', models.ManyToManyField(related_name='learning_users', to='app.Language')),
                ('native_languages', models.ManyToManyField(related_name='native_users', to='app.Language')),
                ('profile_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(to='app.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='Discussion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=1000, null=True)),
                ('description', models.TextField()),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('body', models.TextField()),
                ('comment_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Post')),
                ('comment_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Call',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.DurationField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('call_receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='calls_received', to=settings.AUTH_USER_MODEL)),
                ('call_sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='calls_sent', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
