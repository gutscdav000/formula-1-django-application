
from django import template

register = template.Library()


@register.filter
def get_range(value):
    return range(value)

@register.filter
def index(value, arg):
    return value[arg]

# @register.filter
# def index_value():
