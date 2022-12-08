from django.db import models

# Create your models here.
class Member(models.Model):
    mem_id = models.CharField(primary_key=True, max_length=10)
    mem_name = models.CharField(max_length=10)
    mem_birth = models.DateTimeField()
    mem_mail_addr = models.CharField(max_length=50)
    mem_phone = models.CharField(max_length=13)
    m_status = models.CharField(max_length=1)
    m_pwd = models.CharField(max_length=20)
    dept_cd = models.CharField(max_length=10)
    auth_cd = models.CharField(max_length=2)
    job_title_cd = models.CharField(max_length=10)
    position_cd = models.CharField(max_length=10)
    create_dt = models.DateTimeField(auto_now_add=True) # 해당 레코드 생성시 현재 시간 자동 저장
    modify_dt = models.DateTimeField(auto_now=True) # 해당 레코드 갱신시 현재 시간 자동 저장
    join_dt = models.DateTimeField()
    resign_dt = models.DateTimeField()

    class Meta:
        db_table = 'member'