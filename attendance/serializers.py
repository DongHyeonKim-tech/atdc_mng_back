from rest_framework import serializers
from attendance.models import AccessRecorder, AttendanceStatusCd

class AccessRecorderSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessRecorder
        # fields = '__all__'
        fields = ('recorder_id', 'office_nm')

class AttendanceStatusCdSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceStatusCd
        # fields = '__all__'
        fields = ("attd_cd_id", "top_attd_cd_id", "attd_cd", "attd_cd_expl", "deduction_days", "use_yn")