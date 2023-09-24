# Generated by Django 4.2.5 on 2023-09-23 21:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0003_alter_lessonlearning_watched_sec'),
    ]

    operations = [
        migrations.AddField(
            model_name='productpurchase',
            name='buyer',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
