# Generated by Django 3.1.7 on 2021-03-23 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20210323_0611'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='timejoin',
            new_name='join_at',
        ),
        migrations.AlterField(
            model_name='profile',
            name='spicial',
            field=models.CharField(choices=[('جلديه', 'جلديه'), ('باطنه', 'باطنه'), ('قلب', 'قلب'), ('عظام', 'عظام'), ('كبد', 'كبد'), ('اوعيه', 'اوعيه'), ('اسنان', 'اسنان')], max_length=50, verbose_name='التخصص'),
        ),
    ]
