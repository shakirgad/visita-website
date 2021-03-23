# Generated by Django 3.1.7 on 2021-03-23 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20210323_0607'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='time_add',
            new_name='timejoin',
        ),
        migrations.AlterField(
            model_name='profile',
            name='spicial',
            field=models.CharField(choices=[('باطنه', 'باطنه'), ('اسنان', 'اسنان'), ('كبد', 'كبد'), ('جلديه', 'جلديه'), ('اوعيه', 'اوعيه'), ('عظام', 'عظام'), ('قلب', 'قلب')], max_length=50, verbose_name='التخصص'),
        ),
    ]
