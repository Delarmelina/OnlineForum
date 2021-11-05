from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .forms import PostForm
from django.contrib.auth.models import User

from Forum.models import Post

# Create your views here.
def home(request):

    posts_list = Post.objects.all().order_by('-created_at')

    paginator = Paginator(posts_list, 10)

    page = request.GET.get('page')

    posts = paginator.get_page(page)

    return render(request, './home.html', {'posts': posts})

def post(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, './post.html', {'post': post})

def newPost(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.title = post.title.upper()
            post.author = request.user
            post.keyWords = post.keyWords.lower()
            post.save()
            return redirect('/')
    else:
        form = PostForm()
        return render(request, './newPost.html', {'form': form})

def keyWords(request):
    posts = Post.objects.all()

    keytemp = []
    keys = []

    for post in posts:
        keytemp.append(post.keyWords.split(','))

    for a in keytemp:
        for b in a:
            keys.append(b)
    keys = sorted(set(keys))

    return render(request, './keyWords.html', {'keys': keys})

def search(request, kw):

    # 0 = KeyWords // 1 = Title // 2 = Author // 3 = Content 

    search_by = request.GET.get('type_search')

    if search_by == '0':
        posts = Post.objects.filter(keyWords__contains=kw)
    elif search_by == '1':
        posts = Post.objects.filter(title__contains=kw)
    elif search_by == '2':
        posts = Post.objects.filter(author__username__contains=kw)
    elif search_by == '3':
        posts = Post.objects.filter(content__contains=kw)

    return render(request, './search.html', {'posts': posts})