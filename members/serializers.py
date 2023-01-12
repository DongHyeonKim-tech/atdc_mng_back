from rest_framework import serializers
from .models import Member, PositionCd, DepartmentCd

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = "__all__"


class PositionCdSerializer(serializers.ModelSerializer) :
    class Meta:
        model = PositionCd
        fields = "__all__"

class DepartmentCdSerializer(serializers.ModelSerializer) :
    class Meta:
        model = DepartmentCd
        fields = "__all__"



