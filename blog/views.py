from django.shortcuts import render , redirect , reverse
from .models import Post
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .forms import PostForm
from django.views import generic
from django.urls import reverse_lazy

# def post_list_view(request):
#     # posts_list = Post.objects.all()
#     posts_list = Post.objects.filter(status='PUB').order_by('-date_modified')
#
#     return render(request, 'blog/posts_list.html', {'post_list': posts_list})


class PostListView(generic.ListView): # this is made based on class view
    # model= Post # this model used when we want to have .objects.get.all
    template_name ='blog/posts_list.html'
    context_object_name='post_list'
    def get_queryset(self):
        return Post.objects.filter(status='PUB').order_by('-date_modified')


# def post_detail_view(request,pk):
#     post_detail=get_object_or_404(Post,pk=pk)
#     # try:
#     #     post_detail = Post.objects.get(pk=pk)
#     # except Post.DoesNotExist:
#     # # except ObjectDoesNotExist:
#     #
#     #     post_detail = None
#     #     print('excepeted')
#
#     return render(request, 'blog/post_detail.html', {'post_detail': post_detail})


class PostDetailView(generic.DetailView): #this is made based on class view
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name='post_detail'


# def add_post_view(request): # This view is made based on functional view method
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # return redirect(reverse('post_list_view'))
#             return redirect('post_list_view')
#     else:
#         form = PostForm()
#
#     return render(request, 'blog/add_post.html',context={'form': form })


class AddPostView(generic.CreateView): # this is made based on class view
    template_name= 'blog/add_post.html'
    form_class=PostForm

# def update_view(request, pk):
#     post_update = get_object_or_404(Post, pk=pk)
#
#     form = PostForm(request.POST or None, instance=post_update)
#     if form.is_valid():
#         form.save()
#         return redirect('post_list_view')
#
#     return render(request, 'blog/add_post.html', context={'form': form})

class PostUpdateView(generic.UpdateView):
    template_name='blog/add_post.html'
    form_class=PostForm
    context_object_name= 'form'
    model=Post


# def post_delete_view(request,pk):
#     post_delete = get_object_or_404(Post, pk=pk)
#     if request.method == 'POST':
#         post_delete.delete()
#         return redirect('post_list_view')
#
#     return render (request,'blog/post_delete.html',{'post_delete':post_delete})


class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('post_list_view')
    # form_class = PostForm
    # context_object_name = 'post_delete'

    # def get_success_url(self):
    #     return reverse('post_list_view')
