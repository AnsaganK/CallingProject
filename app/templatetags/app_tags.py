from django import template
from datetime import datetime

register = template.Library()


@register.filter(name='isNull')
def isNull(object):
    return object if object else '-'


@register.filter(name='todayCount')
def todayCount(object):
    today_date = datetime.today()
    print(today_date)
    return object.created_check_lists.filter(date__date=today_date.date()).count()