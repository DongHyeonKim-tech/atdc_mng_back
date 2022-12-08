from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.
class MemberManager(BaseUserManager) :
    def create_user(self, mem_id, password=None):
        """
        주어진 mem_id와 password로 Member 인스턴스 생성
        """
        if not mem_id:
            raise ValueError(_('Members must have an mem_id'))

        member = self.model(
            mem_id=mem_id
        )
        member.set_password(password)
        member.save(using=self._db)
        return member

    def create_superuser(self, mem_id, password=None) :
        """
        주어진 mem_id와 password로 Member 인스턴스 생성
        단, 최상위 사용자이므로 권한을 부여
        """
        member = self.create_user(
            mem_id=mem_id,
            password=password
        )
        member.is_admin = True
        member.save(using=self._db)
        return member

class Member(AbstractBaseUser):
    mem_id = models.CharField("아이디", primary_key=True, max_length=10)
    mem_name = models.CharField("이름", max_length=10, null=True)
    mem_birth = models.DateTimeField("생년월일", null=True)
    mem_mail_addr = models.EmailField("이메일", max_length=100, unique=True, null=True)
    mem_phone = models.CharField("전화번호", max_length=13, null=True)
    mem_status = models.BooleanField("계정상태", default=True)
    is_admin = models.BooleanField("관리자 여부", default=False)
    team_cd = models.CharField("팀 코드", max_length=10, null=True)
    auth_cd = models.CharField("권한코드", max_length=10, null=True)
    position_cd = models.CharField("직책코드", max_length=10, null=True)
    create_dt = models.DateTimeField("가입일", auto_now_add=True) # 해당 레코드 생성시 현재 시간 자동 저장
    modify_dt = models.DateTimeField("수정일", auto_now=True) # 해당 레코드 갱신시 현재 시간 자동 저장
    join_dt = models.DateTimeField("입사일", null=True)
    resign_dt = models.DateTimeField("퇴사일", null=True)

    USERNAME_FIELD = 'mem_id'

    object = MemberManager()

    class Meta:
        db_table = 'member'

    def __str__(self):
        return self.mem_name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    @property
    def is_staff(self) :
        return self.is_admin