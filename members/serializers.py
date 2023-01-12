from rest_framework import serializers
from .models import Member, PositionCd, DepartmentCd

class MemberCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ("mem_id", )

# 직책 생성용 시리얼라이저
class PositionCdCreateSerializer(serializers.ModelSerializer) :
    class Meta:
        model = PositionCd
        fields = ("position_cd", "position_nm")

# 직책 조회용 시리얼라이저
class PositionCdSerializer(serializers.ModelSerializer) :
    class Meta:
        model = PositionCd
        fields = ("id", "position_cd", "position_nm")

# 부서 생성용 시리얼라이저
class DepartmentCdCreateSerializer(serializers.ModelSerializer) :
    class Meta:
        model = DepartmentCd
        fields = ("dept_cd", "dept_nm", "top_dept_cd")

# 부서 조회용 시리얼라이저
class DepartmentCdSerializer(serializers.ModelSerializer) :
    class Meta:
        model = DepartmentCd
        fields = ("dept_cd", "dept_nm", "top_dept_cd")



