from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from django.shortcuts import get_object_or_404
from .forms import PostForm, EditForm, CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse


# def home(request):
# return render(request, 'home.html', {})


def LikeView(requset, pk):
    post = get_object_or_404(Post, id=requset.POST.get('post_id'))
    post.likes.add(requset.user)
    return HttpResponseRedirect(reverse('article_details', args=[str(pk)]))


class HomeView(ListView):
    model = Post
    template_name = "home.html"
    # ordering = ['-post_date']
    # ordering = ['-id']


class ArticleDetailView(DetailView):
    model = Post
    template_name = "article_details.html"


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = "update_post.html"


class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy('home')


class AddCategoryView(CreateView):
    model = Category
    template_name = "add_category.html"
    fields = "__all__"


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "add_comment.html"
    #fields = "__all__"
    success_url = reverse_lazy("home")

