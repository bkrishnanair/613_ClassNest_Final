from django import template

register = template.Library()

@register.filter
def is_instructor(user):
    return user.groups.filter(name='Instructor').exists()
