from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, APIView
from rest_framework.generics import get_object_or_404
from .models import Member, PositionCd, DepartmentCd
from .serializers import (
                            MemberCreateSerializer, 
                            PositionCdSerializer, 
                            PositionCdCreateSerializer,
                            DepartmentCdSerializer, 
                            DepartmentCdCreateSerializer,
                        )

# TODO: 
# 사원번호 중복검사 api, 
# 사원번호 자동완성 api


# ============================================================================
# 직책
class PositionsView(APIView):
    # 직책 코드 등록
    def post(self, request) :
        """
        직책 생성 뷰
        """
        serializer = PositionCdCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            position_obj = PositionCd.objects.get(position_cd = request.data['position_cd'])
            serializer = PositionCdCreateSerializer(position_obj, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self):
        """ 직책 전체 조회 뷰 """
        position_obj = PositionCd.objects.all()
        serializer = PositionCdSerializer(position_obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PositionView(APIView):
    def get(self, request, pk):
        """ 직책 상세 조회 뷰 """
        position_obj = get_object_or_404(PositionCd, id=pk)
        serializer = PositionCdSerializer(position_obj)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk) :
        """ 직책 수정 뷰 """
        position_obj = get_object_or_404(PositionCd, id=pk)
        serializer = PositionCdCreateSerializer(position_obj, data=request.data)
        if serializer.is_valid() :
            serializer.saver()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk) :
        """ 직책 삭제 뷰 """
        position_obj = PositionCd.objects.get(id=pk)
        position_obj.remove()
        return Response({"message":"Delete complete"}, status=status.HTTP_200_OK)

# ============================================================================
# 부서
class DepartmentsView(APIView) :
    def post(self, request):
        """부서 생성 뷰"""
        serializer = DepartmentCdCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def get(self) :
        """부서 전체 조회 뷰"""
        department_obj = DepartmentCd.objects.all()
        serializer = DepartmentCdSerializer(department_obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

class DepartmentView(APIView) :
    def get(self, request, pk) :
        """부서 상세 조회 뷰"""
        department_obj = get_object_or_404(DepartmentCd, id=pk)
        serializer = DepartmentCdSerializer(department_obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk) :
        """ 부서 수정 뷰 """
        department_obj = get_object_or_404(DepartmentCd, id=pk)
        serializer = DepartmentCdCreateSerializer(department_obj, data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk) :
        """ 부서 삭제 뷰 """
        department_obj = DepartmentCd.objects.get(id=pk)
        department_obj.remove()
        return Response({"message":"Delete complete"}, status=status.HTTP_200_OK)

# ============================================================================
# 사원
# class MebersView(APIView) :
#     def post(self, request) :
#         """맴버 등록 뷰"""
#         # serializer = 
#         pass

# @api_view(["POST"])
# def regist_member(request):
#     """
#     멤버 등록 뷰
#     {
#         "mem_id":,
#         "user" :,
#         "dept_cd":,
#         "position_cd":,
#         "mem_name":,
#         "mem_birth":,
#         "mem_mail_addr":,
#         "mem_phone":,
#         "acc_recorder_id":,
#         "join_dt":,
#         "resign_dt":
#     }
#     """
#     serializer = MemberSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(["POST"])
# def create_department_cd(request):
#     """
#     부서 생성 뷰
#     """
#     serializer = DepartmentCdSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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