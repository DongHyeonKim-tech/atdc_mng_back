# Generated by Django 4.1.2 on 2022-12-08 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_alter_member_managers'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='관리자 여부'),
        ),
    ]
