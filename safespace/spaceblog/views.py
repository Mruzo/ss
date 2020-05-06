from django.shortcuts import render
from .models import Post, Like
from django.http import HttpResponse

# Create your views here.


def index(request):
    posts = Post.objects.all()
    return render(request, 'spaceblog/index.html', {'posts': posts})

def likePost(request):
    if request.method == 'GET':
        post_id = request.GET['post_id']
        likedpost = Post.objects.get(pk=post_id)
        m = Like(post=likedpost)
        m.save()
        return HttpResponse("Success!")
    else:
        return HttpResponse("Request method is not a GET")
