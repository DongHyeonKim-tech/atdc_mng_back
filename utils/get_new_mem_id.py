import datetime
from members.models import Member
from django.db.models import Count

def get_new_mem_id():
    # _year = datetime.datetime.now().strftime("%Y")
    _year = "2021"
    member = Member.objects.filter(join_dt__year=_year)
    mem_id = "ES" + _year[:2]

    return mem_id


if __name__ == "__main__" :
    print(get_new_mem_id())
