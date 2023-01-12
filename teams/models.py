from django.db import models
from members.models import Member
from attendance.models import AttendanceSettings



class Team(models.Model):
    team_cd = models.CharField(unique=True,max_length=10, help_text='팀 코드')
    lead_mem_id = models.ForeignKey(Member, null=True, blank=True, related_name='team', on_delete=models.SET_NULL, help_text='팀장')
    team_nm = models.CharField(max_length=20, null=True, blank=True, help_text='팀 이름')
    team_desc = models.CharField(max_length=300, null=True, blank=True, help_text='팀 설명')
    work_addr = models.CharField(max_length=300, null=True, blank=True, help_text='근무지')
    create_dt = models.DateTimeField(auto_now_add=True, help_text="등록일") # 해당 레코드 생성시 현재 시간 자동 저장
    regist_mem_id = models.ForeignKey(Member, related_name='team_regist', null=True, blank=True, on_delete=models.SET_NULL, help_text='등록자')
    modify_dt = models.DateTimeField(auto_now=True, help_text="수정일") # 해당 레코드 갱신시 현재 시간 자동 저장
    modify_mem_id = models.ForeignKey(Member, related_name='team_modify', null=True, blank=True, on_delete=models.SET_NULL, help_text='수정자')
    use_yn = models.BooleanField(null=False, blank=False, default=True, help_text='사용 여부') # True = 사용, False = 사용안함

    class Meta:
        db_table = 'team'

    def __str__(self) -> str:
        return self.team_nm

class TeamMembers(models.Model):
    mem_id = models.ForeignKey(Member, related_name='team_members', on_delete=models.SET_NULL, null=True, blank=True, help_text='팀원')
    team_cd = models.ForeignKey(Team, related_name='team_members', on_delete=models.SET_NULL, null=True, blank=True, help_text='팀코드')
    create_dt = models.DateTimeField(auto_now_add=True, help_text="등록일") # 해당 레코드 생성시 현재 시간 자동 저장
    regist_mem_id = models.ForeignKey(Member, related_name='team_members_regist', null=True, blank=True, on_delete=models.SET_NULL, help_text='등록자')
    modify_dt = models.DateTimeField(auto_now=True, help_text="수정일") # 해당 레코드 갱신시 현재 시간 자동 저장
    modify_mem_id = models.ForeignKey(Member, related_name='team_members_modify', null=True, blank=True, on_delete=models.SET_NULL, help_text='수정자')
    use_yn = models.BooleanField(null=False, blank=False, default=True, help_text='사용 여부') # True = 사용, False = 사용안함

    class Meta:
        db_table = 'team_members'

    def __str__(self) -> str:
        return self.mem_id