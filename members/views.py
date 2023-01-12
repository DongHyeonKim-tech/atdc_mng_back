from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, APIView
from rest_framework.generics import get_object_or_404
from .models import Member, PositionCd
from .serializers import MemberSerializer, PositionCdSerializer, DepartmentCdSerializer
# from members.serializers import MemberSignupSerializer

@api_view(["POST"])
def regist_member(request):
    """
    멤버 등록 뷰
    {
        "mem_id":,
        "user" :,
        "dept_cd":,
        "position_cd":,
        "mem_name":,
        "mem_birth":,
        "mem_mail_addr":,
        "mem_phone":,
        "acc_recorder_id":,
        "join_dt":,
        "resign_dt":
    }
    """
    serializer = MemberSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(["POST"])
# def create_position_cd(request):
#     """
#     직책 생성 뷰
#     """
#     serializer = PositionCdSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PositionView(APIView):
    # 직책 코드 등록
    def post(self, request) :
        """
        직책 생성 뷰
        """
        serializer = PositionCdSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            position_obj = PositionCd.objects.get(position_cd = request.data['position_cd'])
            serializer = PositionCdSerializer(position_obj, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def get(self):
    #     """
    #     직책 조회 뷰
    #     """
    #     position_obj = PositionCd.objects.all()
    #     serializer = PositionCdSerializer(position_obj, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["POST"])
def create_department_cd(request):
    """
    직책 생성 뷰
    """
    serializer = DepartmentCdSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


