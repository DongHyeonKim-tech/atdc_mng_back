from django.db import models
from members.models import Member


# # 근태 코드
# class AttendanceCd(models.Model):
#     attd_cd = models.CharField(primary_key=True, max_length=20, help_text='근태 코드')
#     attd_cd_expl = models.CharField(max_length=100, null=True, help_text='근태 코드 설명')
#     attd_group_cd = models.CharField(max_length=20, help_text='근태 그룹 코드')
#     attd_group_cd_expl = models.CharField(max_length=100, null=True, help_text='근태 그룹 설명')
#     deduction_days = models.FloatField(null=True, blank=True, help_text="연차 차감 개수")
#     use_yn = models.BooleanField(null=False, blank=False, default=True, help_text='사용 여부') # True : 코드 사용 상태, False : 코드 미사용 상태
#     create_dt = models.DateTimeField(auto_now_add=True, help_text='등록일') # 해당 레코드 생성시 현재 시간 자동 저장
#     modify_dt = models.DateTimeField(auto_now=True, help_text='수정일') # 해당 레코드 갱신시 현재 시간 자동 저장

#     class Meta:
#         db_table = 'attd_cd'

#     def __str__(self) -> str:
#         return self.attd_cd

# 근태 상태 코드
class AttendanceStatusCd(models.Model):
    attd_cd_id = models.AutoField(primary_key=True)
    top_attd_cd_id = models.CharField(max_length=100, null=True, blank=True, help_text="상위코드 아이디")
    attd_cd = models.CharField(max_length=100, null=True, help_text="근태코드명")
    attd_cd_expl = models.CharField(max_length=100, null=True, help_text='근태 코드 설명')
    deduction_days = models.FloatField(null=True, blank=True, help_text="연차 차감 개수")
    use_yn = models.BooleanField(null=False, blank=False, default=True, help_text='사용 여부') # True : 코드 사용 상태, False : 코드 미사용 상태
    create_dt = models.DateTimeField(auto_now_add=True, help_text='등록일') # 해당 레코드 생성시 현재 시간 자동 저장
    modify_dt = models.DateTimeField(auto_now=True, help_text='수정일') # 해당 레코드 갱신시 현재 시간 자동 저장

    class Meta:
        db_table = 'attd_status_cd'

    def __str__(self) -> str:
        return self.attd_cd

# 근태 기록
class AttendanceHistory(models.Model):
    attd_no = models.AutoField(primary_key=True)
    mem_id = models.ForeignKey(Member, related_name='attd_hist', null=True, blank=True, on_delete=models.SET_NULL, help_text='사원 번호')
    modify_mem_id = models.ForeignKey(Member, related_name='attd_hist_modify', null=True, blank=True, on_delete=models.SET_NULL, help_text='수정 사원 번호')
    attd_cd_id = models.ForeignKey(AttendanceStatusCd, related_name='attd_hist', null=True, blank=True, on_delete=models.SET_NULL, help_text='근태 코드')
    hist_class = models.CharField(max_length=20, null=True, blank=True, help_text="기록수단구분")
    attd_start_time = models.DateTimeField(help_text='출근 시간', null=True, blank=True)
    attd_end_time = models.DateTimeField(help_text='퇴근 시간', null=True, blank=True)
    create_dt = models.DateTimeField(auto_now_add=True, help_text='생성일') # 해당 레코드 생성시 현재 시간 자동 저장
    modify_dt = models.DateTimeField(auto_now=True, help_text='수정일') # 해당 레코드 갱신시 현재 시간 자동 저장

    class Meta:
        db_table = 'attd_hist'

    def __str__(self) -> str:
        return self.mem_id

# 휴일 설정
class HolidayInfo(models.Model):
    holiday = models.DateTimeField(primary_key=True, help_text='휴일날짜')
    holiday_nm = models.CharField(max_length=20, null=True, blank=True, help_text='휴일 명칭')
    holiday_type = models.CharField(max_length=10, null=True, blank=True, help_text='휴일 구분')

    class Meta:
        db_table = 'holiday_info'

# 휴가 발생 내역
class VacationInfo(models.Model):
    mem_id = models.ForeignKey(Member, null=True, blank=True, related_name='vacation_info', on_delete=models.SET_NULL, help_text='사원번호')
    regist_mem_id = models.ForeignKey(Member, null=True, blank=True, related_name='vacation_info_regist', on_delete=models.SET_NULL, help_text='등록자')
    modify_mem_id = models.ForeignKey(Member, null=True, blank=True, related_name='vacation_info_modify', on_delete=models.SET_NULL, help_text='수정자')
    base_vacation_amt = models.IntegerField(help_text='기본 휴가 개수')
    add_vacation_amt = models.IntegerField(help_text='추가 휴가 개수')
    vacation_type = models.CharField(max_length=2, help_text='휴가 유형')
    vacation_yr = models.CharField(max_length=5, help_text='연차 년도')
    create_dt = models.DateTimeField(auto_now_add=True, help_text='생성일') # 해당 레코드 생성시 현재 시간 자동 저장
    modify_dt = models.DateTimeField(auto_now=True, help_text='수정일') # 해당 레코드 갱신시 현재 시간 자동 저장

    class Meta:
        db_table = 'vacation_info'

# 휴가 사용 기록
class VacationUseHistory(models.Model):
    vacation_use_no = models.AutoField(primary_key=True, help_text='휴가 사용 기록 번호')
    attd_cd_id = models.ForeignKey(AttendanceStatusCd, null=True, blank=True, related_name='vacation_use_attd_cd', on_delete=models.SET_NULL, help_text="근태코드")
    mem_id = models.ForeignKey(Member, related_name="vacation_use_rec", null=True, blank=True, on_delete=models.SET_NULL, help_text='휴가사용자사원번호')
    appr_yn = models.BooleanField(null=False, blank=False, default=False, help_text='결재 여부') # True = 결재 O, False = 결재 X
    act_yn = models.BooleanField(null=False, blank=False, default=False, help_text='시행 여부') # True = 시행 O, False = 시행 X
    start_dt = models.DateTimeField(null=False, blank=False, help_text='휴가시작일시')
    end_dt = models.DateTimeField(null=False, blank=False, help_text='휴가종료일시')
    use_amt = models.IntegerField(null=False, blank=False, help_text='사용일수')
    use_reason = models.CharField(max_length=300, null=True, blank=True, help_text='휴가사유')
    del_yn = models.BooleanField(null=False, blank=False, default=False, help_text='휴가 기록 폐기 여부') # True = 폐기 O, False = 폐기X
    del_reason = models.CharField(max_length=300, null=True, blank=True, help_text='휴가 기록 폐기 사유')
    create_dt = models.DateTimeField(auto_now_add=True, help_text='생성일') # 해당 레코드 생성시 현재 시간 자동 저장
    modify_dt = models.DateTimeField(auto_now=True, help_text='수정일') # 해당 레코드 갱신시 현재 시간 자동 저장

    class Meta:
        db_table = 'vacation_use_hist'



# 근태 셋팅
class AttendanceSettings(models.Model):
    attd_set_cd = models.CharField(unique=True, max_length=10, help_text='근태 설정 코드')
    attd_set_nm = models.CharField(max_length=20, null=True, help_text='근태 설정 이름')
    tolerance_range = models.IntegerField(null=True, blank=True, help_text="시간 오차 허용범위")
    attd_start_time = models.DateTimeField(null=True, blank=True, help_text='출근 시간')
    attd_end_time = models.DateTimeField(null=True, blank=True, help_text='퇴근 시간')
    am_half_start_time = models.DateTimeField(null=True, blank=True, help_text='오전반차 시작시간')
    am_half_end_time = models.DateTimeField(null=True, blank=True, help_text='오전반차 종료시간')
    pm_half_start_time = models.DateTimeField(null=True, blank=True, help_text='오후반차 시작시간')
    pm_half_end_time = models.DateTimeField(null=True, blank=True, help_text='오후반차 종료시간')
    lunch_start_time = models.DateTimeField(null=True, blank=True, help_text='점심 시작시간')
    lunch_end_time = models.DateTimeField(null=True, blank=True, help_text='점심 종료시간')
    dinner_start_time = models.DateTimeField(null=True, blank=True, help_text='저녁식사 시작시간')
    dinner_end_time = models.DateTimeField(null=True, blank=True, help_text='저녁식사 종료시간')
    morning_attd_start_time = models.DateTimeField(null=True, blank=True, help_text='조기출근 시작시간')
    night_attd_start_time = models.DateTimeField(null=True, blank=True, help_text='야근 시작시간')
    sun_work_yn = models.BooleanField(null=False, blank=False, default=False, help_text='일요일 근무여부')
    mon_work_yn = models.BooleanField(null=False, blank=False, default=True, help_text='월요일 근무여부')
    tue_work_yn = models.BooleanField(null=False, blank=False, default=True, help_text='화요일 근무여부')
    wed_work_yn = models.BooleanField(null=False, blank=False, default=True, help_text='수요일 근무여부')
    thu_work_yn = models.BooleanField(null=False, blank=False, default=True, help_text='목요일 근무여부')
    fri_work_yn = models.BooleanField(null=False, blank=False, default=True, help_text='금요일 근무여부')
    sat_work_yn = models.BooleanField(null=False, blank=False, default=False, help_text='토요일 근무여부')

    class Meta:
        db_table = 'attd_setting'

    def __str__(self) -> str:
        return self.attd_set_nm


# 근태 신청서
class AttendanceDraft(models.Model):
    draft_id = models.AutoField(primary_key=True, help_text='근태신청서번호')
    drafter = models.ForeignKey(Member, null=True, blank=True, related_name='attd_draft', on_delete=models.SET_NULL, help_text='근태신청자')
    attd_cd_id = models.ForeignKey(AttendanceStatusCd, null=True, blank=True, related_name='attd_draft', on_delete=models.SET_NULL, help_text='근태코드')
    draft_reason = models.CharField(max_length=300, null=True, blank=True, help_text='근태 사유')
    appr_status = models.CharField(max_length=2, null=False, blank=False, default='0', help_text='결재 상태') # 
    del_yn = models.BooleanField(null=False, blank=False, default=False, help_text='근태 신청서 폐기 여부') # True = 폐기 O, False = 폐기X
    refer_id = models.CharField(max_length=50,null=True, blank=True, help_text='신청서 참조 대상 목록') # FIXME: 참조 대상 목록, 추후에 알림 등등을 위해서는 따로 테이블을 만드는 것이 좋을 것 같므
    modify_mem_id = models.ForeignKey(Member, null=True, blank=True,  related_name='attd_draft_modify', on_delete=models.SET_NULL, help_text='수정자') 
    create_dt = models.DateTimeField(auto_now_add=True, help_text='생성일') # 해당 레코드 생성시 현재 시간 자동 저장
    modify_dt = models.DateTimeField(auto_now=True, help_text='수정일') # 해당 레코드 갱신시 현재 시간 자동 저장

    class Meta:
        db_table = 'attd_draft'

# 근태 결재
class AttendanceDraftApproval(models.Model):
    appr_no = models.AutoField(primary_key=True, help_text='결재 번호')
    draft_id = models.ForeignKey(AttendanceDraft, related_name='attd_draft_appr', null=True, blank=True, on_delete=models.SET_NULL, help_text='근태신청서번호')
    appr_id = models.ForeignKey(Member, related_name='attd_draft_appr', null=True, blank=True, on_delete=models.SET_NULL, help_text='결재자')
    appr_order = models.IntegerField(null=False, blank=False, help_text='결재순서')
    appr_yn = models.BooleanField(null=False, blank=False, default=False, help_text='결재 여부') # True = 결재 O, False = 결재 X
    appr_dt = models.DateTimeField(null=True, blank=True, help_text='결재일')
    modify_mem_id = models.ForeignKey(Member, related_name='attd_draft_appr_modify', null=True, blank=True, on_delete=models.SET_NULL, help_text='수정자') 
    create_dt = models.DateTimeField(auto_now_add=True, help_text='생성일') # 해당 레코드 생성시 현재 시간 자동 저장
    modify_dt = models.DateTimeField(auto_now=True, help_text='수정일') # 해당 레코드 갱신시 현재 시간 자동 저장

    class Meta:
        db_table = 'attd_draft_appr'

# 단말기 아이디
class AccessRecorder(models.Model):
    recorder_id = models.CharField(primary_key=True, max_length=10, help_text='단말기아이디')
    office_nm = models.CharField(max_length=20, null=True, blank=True, help_text='사무실 이름')
    create_dt = models.DateTimeField(auto_now_add=True, help_text='생성일') # 해당 레코드 생성시 현재 시간 자동 저장
    modify_dt = models.DateTimeField(auto_now=True, help_text='수정일') # 해당 레코드 갱신시 현재 시간 자동 저장

    class Meta:
        db_table = "acc_recorder"

# 단말기 기록
class AccessRecord(models.Model) :
    rec_no = models.AutoField(primary_key=True, help_text='기록 번호')
    recorder_id = models.ForeignKey(AccessRecorder, related_name='acc_rec', null=True, blank=True, on_delete=models.SET_NULL, help_text='단말기아이디')
    mem_id = models.ForeignKey(Member, related_name='acc_rec', null=True, blank=True, on_delete=models.SET_NULL, help_text='출입사원번호')
    acc_mode = models.CharField(max_length=2, null=False, blank=False, help_text='출입구분') # 출근, 퇴근, 식수, 출입 모드
    acc_type = models.CharField(max_length=2, null=False, blank=False, help_text='사용자구분') # 사용자 구분 (일반 / 방문)
    rec_dt = models.CharField(max_length=8, help_text='기록된 날짜')
    rec_time = models.CharField(max_length=6, help_text='기록된 시간')
    remark = models.CharField(max_length=2, null=True, blank=True, help_text='전송 여부') # 기록테이블에서 단말기 기록 테이블로 전송이 되었는지 여부
    create_dt = models.DateTimeField(auto_now_add=True, help_text='생성일') # 해당 레코드 생성시 현재 시간 자동 저장
    modify_dt = models.DateTimeField(auto_now=True, help_text='수정일') # 해당 레코드 갱신시 현재 시간 자동 저장

    class Meta:
        db_table = 'acc_rec'

# 단말기 기록테이블에서 원본을 가져오기 위한 테이블
class AccessRecordRaw(models.Model):
    e_date = models.CharField(max_length=8, help_text='기록된 날짜')
    e_time = models.CharField(max_length=6, help_text='기록된 시간')
    g_id = models.CharField(max_length=15, help_text='단말기 아이디')
    e_id = models.CharField(max_length=15, help_text='사용자 아이디')
    e_name = models.CharField(max_length=20, help_text='사용자 이름')
    e_user = models.CharField(max_length=2, help_text='사용자구분')
    e_mode = models.CharField(max_length=2, help_text='출입구분')
    e_uptime = models.CharField(max_length=14, help_text='단말기에서 전송된 시간')
    remark = models.CharField(max_length=2, null=True, blank=True, help_text='전송 여부') # 기록테이블에서 단말기 기록 테이블로 전송이 되었는지 여부

    class Meta:
        db_table = 'acc_rec_raw'