# Generated by Django 3.0.5 on 2020-12-07 00:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_message_discussion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='discussion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='app.Discussion'),
        ),
    ]
