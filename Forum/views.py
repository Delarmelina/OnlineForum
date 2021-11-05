from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .forms import PostForm
from django.contrib.auth.models import User

from Forum.models import Post

# View para a página principal
def home(request):

    posts = Post.objects.all().order_by('-created_at')

    search_by = request.GET.get('type_search')
    if search_by != None:
        posts = searchFilter(request, posts, search_by)
        return render(request, './search.html', {'posts': posts})

    paginator = Paginator(posts, 5)
    page = request.GET.get('page')

    posts = paginator.get_page(page)       

    return render(request, './home.html', {'posts': posts})

# View para a página de detalhes de um post
def post(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, './post.html', {'post': post})

# View para a página de criação de posts
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

# View para a página das keywords
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

    search_by = request.GET.get('type_search')
    if search_by != None:
        posts = searchFilter(request, posts, search_by)
        return render(request, './search.html', {'posts': posts})

    return render(request, './keyWords.html', {'keys': keys})

# View para a página de busca
def search(request, kw):

    posts = Post.objects.filter(keyWords__contains=kw)

    search_by = request.GET.get('type_search')
    if search_by != None:
        posts = searchFilter(request, posts, search_by)

    return render(request, './search.html', {'posts': posts})



#-----------------------------------------------------------------------------------------------------------------------
# Função da barra de pesquisa
def searchFilter(request, posts, search_by):

    search = request.GET.get('query')

    if search_by == '0':
        posts = Post.objects.filter(keyWords__contains=search)
    elif search_by == '1':
            posts = Post.objects.filter(title__contains=search)
    elif search_by == '2':
        posts = Post.objects.filter(author__username__contains=search)
    elif search_by == '3':
        posts = Post.objects.filter(content__contains=search)

    return posts