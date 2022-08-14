from django import template
from blog.models import Post

register = template.Library()
@register.inclusion_tag('latest.html')

def get_latest_post():
    context = dict()
    context['latest'] = Post.objects.order_by('-date')[:3]
    return context