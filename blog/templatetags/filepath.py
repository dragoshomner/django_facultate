from django import template

register = template.Library()

@register.filter
def filepath(value):
    return value.replace("/blog","")