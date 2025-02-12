from django.shortcuts import render
from .models import Post
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404


def post_list_view(request):
    # posts_list = Post.objects.all()
    posts_list = Post.objects.filter(status='PUB')

    return render(request, 'blog/posts_list.html', {'post_list': posts_list})


def post_detail_view(request,pk):
    post_detail=get_object_or_404(Post,pk=pk)
    # try:
    #     post_detail = Post.objects.get(pk=pk)
    # except Post.DoesNotExist:
    # # except ObjectDoesNotExist:
    #
    #     post_detail = None
    #     print('excepeted')


    return render(request, 'blog/post_detail.html', {'post_detail': post_detail})

# Create your views here.
