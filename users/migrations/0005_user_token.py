# Generated by Django 5.0.4 on 2024-05-22 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='token',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='токен'),
        ),
    ]