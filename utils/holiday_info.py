import requests
import datetime
from bs4 import BeautifulSoup
import pandas as pd



# 윤달이 있는 년도 확인하기
def is_leap(year):
    """
    윤달이 있는 해 : True
    윤달이 없는 해 : False
    """
    leap = False
    if (year > 10**5) or (year < 1990):
        print("Input Error Occurred")
    elif (year%400 == 0):
        leap = True
        return leap
    elif (year%100 == 0):
        leap = False
        return leap
    elif (year%4 == 0):
        leap = True
        return leap
    else:
        leap = False
        return leap

# 휴일 정보 반환 쿼리 생성
def get_request_query(url, operation, params, service_key):
    import urllib.parse as urlparse
    params = urlparse.urlencode(params)
    request_query = url + '/' + operation + '?' + params + '&' + 'serviceKey' + '=' + service_key
    return request_query

# 공공데이터 포털 한국천문연구원_특일 정보 open_api 사용
# https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15012690
holiday_api_key = 'J3t6Tt29JhkMUi%2BBqR7qQwDPzMmzOMHHV%2F12aUzI9jXGIeAwkqGbiBPqyGD5RPCcwinKSCZ%2F0dYYnlvU7HSKlQ%3D%3D'

# 휴일 정보 데이터 프레임 생성
def create_holiday_df(year, holiday_api_key):
    holiday_weekday_dict = {}
    weekdays_kor = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']

    # 모든 달의 날자 갯수 리스트 만들기
    if is_leap(year) == True :
        number_of_month_list = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else :
        number_of_month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # 날짜를 확인하면서 토요일 혹은 일요일인경우 기록 -> 토요일, 일요일 
    for idx, day_cnt in enumerate(number_of_month_list) :
        for cnt in range(1, day_cnt+1):
            day = datetime.date(year, idx+1, cnt)
            weekday = day.weekday()
            if weekday in [5, 6]:
                holiday_weekday_dict[day.strftime('%Y-%m-%d')] = [weekdays_kor[weekday], '공휴일']

    # 공휴일 API에서 가져온 날도 휴일로 기록 -> 공휴일
    for month in range(1,13):
        if month < 10:
            month = "0" + str(month)
        else :
            month = str(month)
        
        url = '	http://apis.data.go.kr/B090041/openapi/service/SpcdeInfoService'

        # 공휴일 정보 조회
        operation = 'getRestDeInfo'

        params = {'solYear': year, 'solMonth': month}
        request_query = get_request_query(url, operation, params, holiday_api_key)
        get_data = requests.get(request_query)

        if get_data.ok == True:
            soup = BeautifulSoup(get_data.content, 'html.parser')
            item = soup.findAll('item')
            # print(item)
            for i in item:
                day = datetime.date(int(year), int(month), int(i.locdate.string[-2:]))
                holiday_weekday_dict[day.strftime('%Y-%m-%d')] = [i.datename.string, '공휴일']

    holiday_df_data = [[i, holiday_weekday_dict[i][0], holiday_weekday_dict[i][1]] for i in holiday_weekday_dict.keys()]

    holiday_df = pd.DataFrame(columns=['holiday', 'holiday_nm', 'holiday_type'], data=holiday_df_data)
    holiday_df = holiday_df.sort_values('holiday')
    return holiday_df