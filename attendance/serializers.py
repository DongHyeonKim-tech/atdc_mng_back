from rest_framework import serializers
from rest_framework.exceptions import ValidationError
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

    def validate(self, attrs):
        if attrs['top_attd_cd_id'] == '0':
            raise ValidationError("근태 상태 코드는 해당 필드 값이 '0'이 아니어야 한다.")
        return super().validate(attrs)

class CreateTopAttendanceStatusCdSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceStatusCd
        fields = ("attd_cd_id", "top_attd_cd_id", "attd_cd", "attd_cd_expl", "use_yn")

    def validate(self, attrs) :
        if attrs['top_attd_cd_id'] != '0' :
            raise ValidationError("근태 상태 그룹코드는 해당 필드 값이 '0' 이어야 한다.")
        return super().validate(attrs)

class TopAttendanceStatusCdSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceStatusCd
        fields = ("attd_cd_id", "attd_cd", "attd_cd_expl")

    