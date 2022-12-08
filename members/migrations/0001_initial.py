# Generated by Django 4.1.2 on 2022-12-08 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('mem_id', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='아이디')),
                ('mem_pwd', models.CharField(max_length=20, verbose_name='비밀번호')),
                ('mem_name', models.CharField(max_length=10, verbose_name='이름')),
                ('mem_birth', models.DateTimeField(verbose_name='생년월일')),
                ('mem_mail_addr', models.EmailField(max_length=100, unique=True, verbose_name='이메일')),
                ('mem_phone', models.CharField(max_length=13, verbose_name='전화번호')),
                ('mem_status', models.BooleanField(default=True, verbose_name='계정상태')),
                ('team_cd', models.CharField(max_length=10, verbose_name='팀 코드')),
                ('auth_cd', models.CharField(max_length=10, verbose_name='권한코드')),
                ('position_cd', models.CharField(max_length=10, verbose_name='직책코드')),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='가입일')),
                ('modify_dt', models.DateTimeField(auto_now=True, verbose_name='수정일')),
                ('join_dt', models.DateTimeField(verbose_name='입사일')),
                ('resign_dt', models.DateTimeField(verbose_name='퇴사일')),
            ],
            options={
                'db_table': 'member',
            },
        ),
    ]