# Generated by Django 3.1.7 on 2021-03-15 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210315_2358'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default=1, upload_to='profile', verbose_name='الصوره'),
            preserve_default=False,
        ),
    ]
