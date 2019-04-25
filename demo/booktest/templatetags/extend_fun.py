from django import template
from ..models import Post
# 得到Django负责管理标签和过滤器的类
register=template.Library()

@register.simple_tag
def getlatestposts():

    return Post.objects.all().dates('create_time','month',order='DESC')


@register.simple_tag
def latest_post(num=3):
    latest_post=Post.objects.all().order_by('-create_time')[:num]
    return latest_post
