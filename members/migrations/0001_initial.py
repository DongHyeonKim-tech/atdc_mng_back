# Generated by Django 4.1.2 on 2022-12-07 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('mem_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('mem_name', models.CharField(max_length=10)),
                ('mem_birth', models.DateTimeField()),
                ('mem_mail_addr', models.CharField(max_length=50)),
                ('mem_phone', models.CharField(max_length=13)),
                ('m_status', models.CharField(max_length=1)),
                ('m_pwd', models.CharField(max_length=20)),
                ('dept_cd', models.CharField(max_length=10)),
                ('auth_cd', models.CharField(max_length=2)),
                ('job_title_cd', models.CharField(max_length=10)),
                ('position_cd', models.CharField(max_length=10)),
                ('create_dt', models.DateTimeField(auto_now_add=True)),
                ('modify_dt', models.DateTimeField(auto_now=True)),
                ('join_dt', models.DateTimeField()),
                ('resign_dt', models.DateTimeField()),
            ],
            options={
                'db_table': 'member',
            },
        ),
    ]
