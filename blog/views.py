from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, EditForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse


def home(request):
    return render(request, 'home.html', {})


def LikeView(requset, pk):
    post = get_object_or_404(Post, id=requset.POST.get('post_id'))
    post.likes.add(requset.user)
    return HttpResponseRedirect(reverse('article_detail', args=[str(pk)]))


class HomeView(ListView):
    model = Post
    template_name = 'home.html'


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = "update_post.html"


    # fields = 'title', 'author', 'text'




















