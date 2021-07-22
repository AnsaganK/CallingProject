from django import template

register = template.Library()


@register.filter(name="isNull")
def isNull(object):
    return object if object else '-'
