# Generated by Django 3.1.7 on 2021-03-23 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20210319_0821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='spicial',
            field=models.CharField(choices=[('عظام', 'عظام'), ('جلديه', 'جلديه'), ('اوعيه', 'اوعيه'), ('كبد', 'كبد'), ('باطنه', 'باطنه'), ('قلب', 'قلب'), ('اسنان', 'اسنان')], max_length=50, verbose_name='التخصص'),
        ),
    ]
