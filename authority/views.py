from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from authority.serializers import UserSignupSerializer

# Create your views here.
class RegisterView(APIView):
    
    # 회원가입
    def post(self, request) :
        serializer = UserSignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message" : "가입완료"})
        else:
            return Response({"message" : f"${serializer.errors}"}, 400)

    # 회원정보 수정
    def put(self, request) :
        return Response({"message" : "put method is ready"})

    # 회원 탈퇴
    def delete(self, request) :
        return Response({"message" : "delete method is ready"})

class AuthPingView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        return Response({'message':'pong'}, status=status.HTTP_200_OK)