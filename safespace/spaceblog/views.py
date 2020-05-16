from django.shortcuts import render
from .models import Post, Like
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.


def index(request):
    posts = Post.objects.all()
    return render(request, 'spaceblog/index.html', {'posts': posts})


class PostListView(ListView):
    model = Post
    template_name = 'spaceblog/index.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['post_heading', 'post_text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['post_heading', 'post_text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/spaceblog'

    def test_func(self):
        post = self.get_object()
        # print(dir(post))
        if self.request.user == post.author:
            return True
        return False


def likePost(request):
    if request.method == 'GET':
        post_id = request.GET['post_id']
        likedpost = Post.objects.get(pk=post_id)
        m = Like(post=likedpost)
        m.save()
        return HttpResponse("Success!")
    else:
        return HttpResponse("Request method is not a GET")
