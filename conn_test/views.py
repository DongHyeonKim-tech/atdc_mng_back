from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def connection_test(request):
    """
    attd_backend 연결을 확인하기 위한 API
    """
    data = dict()
    data['message'] = "attd_backend와의 연결이 확인되었습니다."
    return Response(data)