from django.shortcuts import render, redirect
from .forms import PostForm

from Forum.models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, './home.html', {'posts': posts})

def post(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, './post.html', {'post': post})

def newPost(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/')
    else:
        form = PostForm()
        return render(request, './newPost.html', {'form': form})
