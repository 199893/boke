from django.shortcuts import render,get_object_or_404,redirect,reverse
from django.http import HttpResponse
from .forms import CommentForm
from booktest.models import Post
# Create your views here.

def commitcomment(request,id):
    post=get_object_or_404(Post,pk=id)
    if request.method=='POST':
        comment=CommentForm(request.POST)
        if comment.is_valid():
            comment=comment.save(commit=False)
            comment.post=post
            comment.save()
            return redirect(reverse('blog:single',args=(id,)))
        else:
            return HttpResponse('评论失败')
    else:
        return HttpResponse('评论失败')
