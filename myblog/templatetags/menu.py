from django import template
from myblog.models import Category
from myblog.forms import SubscriptionForm

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.simple_tag()
def get_subscribe():
    return SubscriptionForm
