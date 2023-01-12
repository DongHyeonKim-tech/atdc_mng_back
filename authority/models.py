from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
# from members.models import Member

class UserManager(BaseUserManager) :
    def create_user(self, user_id, password=None):
        """
        주어진 user_id와 password로 User 인스턴스 생성
        """
        if not user_id:
            raise ValueError(_('User must have an user_id'))

        user = self.model(
            user_id=user_id
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, password=None) :
        """
        주어진 user_id와 password로 User 인스턴스 생성
        단, 최상위 사용자이므로 권한을 부여
        """
        user = self.create_user(                                
            user_id=user_id,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class AuthorityCd(models.Model):
    auth_cd = models.CharField(unique=True, max_length=10, help_text='권한 코드')
    auth_nm = models.CharField(max_length=20, null=True, help_text='권한 이름')
    create_dt = models.DateTimeField(auto_now_add=True, help_text='등록일') # 해당 레코드 생성시 현재 시간 자동 저장
    modify_dt = models.DateTimeField(auto_now=True, help_text='수정일') # 해당 레코드 갱신시 현재 시간 자동 저장

    class Meta :
        db_table = 'authority_cd'

    def __str__(self) -> str:
        return self.auth_nm


class User(AbstractBaseUser):
    user_id = models.CharField(primary_key=True, max_length=10, help_text='유저 아이디')
    user_status = models.CharField(max_length=10, null=True, default="0", help_text='계정 상태') # 0 : 정상, 1: 중지, 2:승인대기, 3:삭제
    auth_cd = models.ForeignKey(AuthorityCd, related_name='user', null=True, blank=True, on_delete=models.CASCADE, help_text='권한 코드')
    # mem_id = models.ForeignKey(Member, related_name='user', null=True, blank=True, on_delete=models.CASCADE, help_text='사원 번호')
    is_admin = models.BooleanField("관리자 여부", default=False)
    create_dt = models.DateTimeField(auto_now_add=True, help_text='등록일') # 해당 레코드 생성시 현재 시간 자동 저장
    modify_dt = models.DateTimeField(auto_now=True, help_text='수정일') # 해당 레코드 갱신시 현재 시간 자동 저장

    class Meta :
        db_table = 'user'

    USERNAME_FIELD = 'user_id'

    objects = UserManager()

    def __str__(self) -> str:
        return self.user_id

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


