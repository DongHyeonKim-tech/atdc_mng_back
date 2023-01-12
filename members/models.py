from django.db import models
from authority.models import User
from attendance.models import AttendanceSettings

# 직책 코드
class PositionCd(models.Model):
    position_cd = models.CharField(unique=True, max_length=10, help_text='직책 코드')
    position_nm = models.CharField(max_length=20, null=True, help_text='직책 이름')
    create_dt = models.DateTimeField(auto_now_add=True, help_text="등록일") # 해당 레코드 생성시 현재 시간 자동 저장
    modify_dt = models.DateTimeField(auto_now=True, help_text="수정일") # 해당 레코드 갱신시 현재 시간 자동 저장

    class Meta:
        db_table = 'position_cd'

    def __str__(self) -> str:
        return self.position_nm

# 부서 코드
class DepartmentCd(models.Model):
    dept_cd = models.CharField(unique=True, max_length=10, help_text='부서코드')
    dept_nm = models.CharField(max_length=30, null=True, blank=True, help_text='부서이름')
    top_dept_cd = models.CharField(max_length=10, null=True, blank=True, help_text='상급부서 코드')
    create_dt = models.DateTimeField(auto_now_add=True, help_text='등록일') # 해당 레코드 생성시 현재 시간 자동 저장
    modify_dt = models.DateTimeField(auto_now=True, help_text='수정일') # 해당 레코드 갱신시 현재 시간 자동 저장

    class Meta:
        db_table = 'department_cd'

    def __str__(self) -> str:
        return self.dept_nm

# 사원 테이블
class Member(models.Model):
    mem_id = models.CharField(unique=True, max_length=10, help_text='사원번호')
    user = models.OneToOneField(User, null=True, blank=True, related_name="member_user_id", on_delete=models.CASCADE)
    dept_cd = models.ForeignKey(DepartmentCd, null=True, blank=True, related_name='member', on_delete=models.SET_NULL, help_text='부서코드')
    position_cd = models.ForeignKey(PositionCd, null=True, blank=True, related_name='member', on_delete=models.SET_NULL, help_text='직책코드')
    attd_set_cd = models.OneToOneField(AttendanceSettings, null=True, blank=True, related_name='member_attd', on_delete=models.SET_NULL, help_text='근태설정 코드') # FIXME: 근태 셋팅을 어디서 설정해야 할지 좀 더 고민이 필요하다.
    mem_name = models.CharField(max_length=10, null=True, help_text='사원이름')
    mem_birth = models.DateTimeField(null=True, help_text='생년월일')
    mem_mail_addr = models.EmailField(max_length=100, unique=True, null=True, help_text='이메일')
    mem_phone = models.CharField(max_length=13, null=True, help_text='전화번호')
    acc_recorder_id = models.CharField(max_length=10, null=False, unique=True, help_text='출입기록 단말기 아이디')
    create_dt = models.DateTimeField(auto_now_add=True, help_text='등록일') # 해당 레코드 생성시 현재 시간 자동 저장
    modify_dt = models.DateTimeField(auto_now=True, help_text='수정일') # 해당 레코드 갱신시 현재 시간 자동 저장
    join_dt = models.DateTimeField(null=True, help_text='입사일')
    resign_dt = models.DateTimeField(null=True, help_text='퇴사일')

    class Meta:
        db_table = 'member'

    def __str__(self) -> str:
        return self.mem_name








# class PositionMapping(models.Model):
#     mem_id = models.ForeignKey('Member', related_name='position_mapping', on_delete=models.SET_NULL, null=True)
#     position_cd = models.ForeignKey('PositionCd', related_name='position_mapping', on_delete=models.SET_NULL, null=True)

#     class Meta:
#         db_table = 'position_mapping'