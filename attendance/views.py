from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from .models import AttendanceStatusCd, AccessRecorder
from .serializers import (
                            AccessRecorderSerializer, 
                            AttendanceStatusCdSerializer, 
                            CreateTopAttendanceStatusCdSerializer, 
                            TopAttendanceStatusCdSerializer
                        )

class AccRecorderInfoView(APIView):
    def post(self, request):
        """
        캡스 기기 아이디 등록 뷰
        request_form :
        {
            "recorder_id" : "1",
            "office_nm" : "대동_연구소"
        }
        """
        serializer = AccessRecorderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        """캡스 기기 아이디 전체 조회 뷰"""
        acc_rec_obj = AccessRecorder.objects.all()
        serializer = AccessRecorderSerializer(acc_rec_obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AccRecorderInfoDetailView(APIView):
    def put(self,request, recorder_id):
        """캡스 기기 아이디 수정 뷰"""
        acc_rec_obj = get_object_or_404(AccessRecorder, recorder_id=recorder_id)
        serializer = AccessRecorderSerializer(acc_rec_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, recorder_id):
        """캡스 기기 아이디 삭제 뷰"""
        acc_rec_obj = AccessRecorder.objects.get(recorder_id=recorder_id)
        acc_rec_obj.remove()
        return Response({"message":"Delete complete"}, status=status.HTTP_200_OK)

class AttdStatusCdView(APIView):
    def post(self, request):
        """
        근태 상태 코드 생성 뷰
        request_form :
        {
            "top_attd_cd_id" : 1, 
            "attd_cd" : "출근", 
            "attd_cd_expl" : "출근", 
            "deduction_days" : 0, 
            "use_yn" : "True"
        }
        """                         
        serializer = AttendanceStatusCdSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        """근태 상태 코드 전체 조회 뷰"""
        attd_status_cd_obj = AttendanceStatusCd.objects.all()
        serializer = AttendanceStatusCdSerializer(attd_status_cd_obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AttdStatusCdDetailView(APIView):
    def get(self, request, attd_cd_id):
        """근태 상태 코드 상세 조회 뷰"""
        attd_status_cd_obj = get_object_or_404(AttendanceStatusCd, attd_cd_id=attd_cd_id)
        serializer = AttendanceStatusCdSerializer(attd_status_cd_obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, attd_cd_id):
        """근태 상태 코드 수정 뷰"""
        attd_status_cd_obj = get_object_or_404(AttendanceStatusCd, attd_cd_id=attd_cd_id)
        serializer = AttendanceStatusCdSerializer(attd_status_cd_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, attd_cd_id):
        """근태 상태 코드 삭제 뷰"""
        attd_status_cd_obj = AttendanceStatusCd.objects.get(attd_cd_id=attd_cd_id)
        attd_status_cd_obj.remove()
        return Response({"message":"Delete complete"}, status=status.HTTP_200_OK)


class TopAttdStatusCdView(APIView):
    def get(self, request):
        """근태 상태 코드 그룹 전체 조회"""
        attd_status_cd_obj = AttendanceStatusCd.objects.filter(top_attd_cd_id='0')
        serializer = TopAttendanceStatusCdSerializer(attd_status_cd_obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """근태 상태 코드 그룹 생성"""
        serializer = CreateTopAttendanceStatusCdSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


class TopAttdStatusCdDetailView(APIView):
    def put(self, request, attd_cd_id):
        """근태 상태 코드 그룹 수정"""
        attd_status_cd_obj = get_object_or_404(AttendanceStatusCd, attd_cd_id=attd_cd_id)
        serializer = CreateTopAttendanceStatusCdSerializer(attd_status_cd_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)













# @api_view(["GET"])
# def get_top_attd_cd(request):
#     # attd_status_cd_obj = get_object_or_404(AttendanceStatusCd, top_attd_cd_id=0)
#     attd_status_cd_obj = AttendanceStatusCd.objects.filter(top_attd_cd_id='0')
#     serializer = AttendanceStatusCdTopSerializer(attd_status_cd_obj, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)





        




# @api_view(['POST'])
# def create_attd_status_cd(request):
#     """
#     근태 상태 코드 생성 뷰
#     request_form :
#     {
#         "top_attd_cd_id" : 1, 
#         "attd_cd" : "출근", 
#         "attd_cd_expl" : "출근", 
#         "deduction_days" : 0, 
#         "use_yn" : "True"
#     }
#     """                         
#     serializer = AttendanceStatusCdSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# def edit_attd_status_cd(request):
#     """
#     근태 상태 코드 수정 뷰
#     {
#         "attd_cd_id" : 3, 
#         "top_attd_cd_id": 1, 
#         "attd_cd" : "출근", 
#         "attd_cd_expl" : "출근", 
#         "deduction_days" : 0, 
#         "use_yn" : "True"
#     }
#     """
#     attd_cd_id = request.data["attd_cd_id"]
#     print("attd_cd_id : ",attd_cd_id)
#     attd_status_cd = get_object_or_404(AttendanceStatusCd, attd_cd_id=attd_cd_id)
#     serializer = AttendanceStatusCdSerializer(attd_status_cd, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# def create_acc_recorder_info(request):
#     """
#     캡스 기기 아이디 등록 뷰
#     request_form :
#     {
#         "recorder_id" : "1",
#         "office_nm" : "대동_연구소"
#     }
#     """
#     serializer = AccessRecorderSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)