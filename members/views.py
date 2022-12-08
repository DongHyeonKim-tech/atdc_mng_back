from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from members.serializers import MemberSignupSerializer

class MemberView(APIView):
    
    # 사용자 정보 조회
    def get(self, request) :
        return Response(MemberSignupSerializer(request.mem_id).data, status=status.HTTP_200_OK)

    # 회원가입
    def post(self, request) :
        serializer = MemberSignupSerializer(data=request.data)
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
