from django import template

from contact.models import ContactLink, About

register = template.Library()

@register.simple_tag()
def get_social_links():
    return ContactLink.objects.all()

@register.simple_tag()
def get_about():
    return About.objects.last()