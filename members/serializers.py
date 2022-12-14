from rest_framework import serializers
from members.models import Member as MemberModel

class MemberSignupSerializer(serializers.ModelSerializer) :
    class Meta :
        model = MemberModel
        fields = "__all__"

    def create(self, *args, **kargs): # 패스워드를 해싱해서 받기 위한 작업
        member = super().create(*args, **kargs)
        password = member.password
        member.set_password(password)
        member.save()
        return member

    def update(self, *args, **kargs): # 패스워드를 해싱해서 받기 위한 작업
        member = super().create(*args, **kargs)
        password = member.password
        member.set_password(password)
        member.save()
        return member


