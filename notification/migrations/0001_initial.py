# Generated by Django 3.0.7 on 2020-06-11 18:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tweet', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notified_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('tweet_visibility', models.BooleanField(default=True)),
                ('notified_tweet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tweet.Tweet')),
                ('target_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
