from django.shortcuts import render,reverse,redirect,get_list_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Category,Tag,Post
# Create your views here.
from comment.forms import CommentForm
from django.core.paginator import Paginator

def index(request):
    book=Post.objects.all()
    category=Category.objects.all()
    tag=Tag.objects.all()
    paginator=Paginator(book,2)
    pagenum=request.GET.get('page')
    pagenum=1 if pagenum==None else pagenum
    page=paginator.page(pagenum)
    return render(request,'booktest/index.html',{'book':book,'category':category,'tag':tag,'page':page})

def single(request,id):
    book=Post.objects.get(pk=id)
    category = Category.objects.all()
    tag = Tag.objects.all()
    # return HttpResponse('123')
    form=CommentForm()
    return render(request,'booktest/single.html',{'book':book,'category':category,'tag':tag,'form':form})


def category(request,id):
    cl = Category.objects.get(pk=id)
    cll = cl.post_set.all()
    category = Category.objects.all()
    tag = Tag.objects.all()
    return render(request,'booktest/category.html',{'cll':cll,'category':category,'tag':tag})

def tag(request,id):
    ta = Tag.objects.get(pk=id)
    taa = ta.post_set.all()
    category = Category.objects.all()
    tag = Tag.objects.all()
    return render(request,'booktest/tag.html',{'taa':taa,'category':category,'tag':tag})

def archives(request,y,m):
    postlist = get_list_or_404(Post, create_time__year = y, create_time__month = m)
    context = {
        "postlist":postlist,
    }
    return render(request,'booktest/index.html',context)

