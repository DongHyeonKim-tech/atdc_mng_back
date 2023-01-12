from rest_framework import serializers
from authority.models import User as UserModel 

class UserSignupSerializer(serializers.ModelSerializer) :
    class Meta :
        model = UserModel
        fields = "__all__"

    def create(self, *args, **kargs): # 패스워드를 해싱해서 받기 위한 작업
        user = super().create(*args, **kargs)
        password = user.password
        user.set_password(password)
        user.save()
        return user

    def update(self, *args, **kargs): # 패스워드를 해싱해서 받기 위한 작업
        user = super().create(*args, **kargs)
        password = user.password
        user.set_password(password)
        user.save()
        return user
