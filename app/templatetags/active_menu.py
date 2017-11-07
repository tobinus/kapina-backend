import re
from django import template
from django.core.urlresolvers import reverse, NoReverseMatch

register = template.Library()


@register.simple_tag(takes_context=True)
def active(context, url_name):
    try:
        pattern = reverse(url_name)
    except NoReverseMatch:
        print('No reverse match for ' + url_name)
        return ''
    path = context['request'].path
    if re.search(pattern, path):
        return 'selected'
    return ''
