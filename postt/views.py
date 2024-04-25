from django.shortcuts import render
from django.core.paginator import Paginator
from postt.models import Post,Page
from django.db.models import Q

# Create your views here.


PER_PAGE = 9

def idx(request):
    posts = Post.objects.get_published()

    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'postt/pages/idx.html',
        {
            'page_obj': page_obj,
        }
    )

def created_by(request, author_pk):
    posts = Post.objects.get_published()\
        .filter(created_by__pk=author_pk)

    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'postt/pages/idx.html',
        {
            'page_obj': page_obj,
        }
    )

def search(request):
    search_value = request.GET.get('search', '').strip()

    posts = (
        Post.objects.get_published()
        .filter(
            Q(title__icontains=search_value) |
            Q(excerpt__icontains=search_value) |
            Q(content__icontains=search_value)
        )[:PER_PAGE]
    )

    return render(
        request,
        'postt/pages/idx.html',
        {
            'page_obj': posts,
            'search_value': search_value,
        }
    )

def categoryy(request, slug):
    posts = Post.objects.get_published()\
        .filter(categoryy__slug=slug)

    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'postt/pages/idx.html',
        {
            'page_obj': page_obj,
        }
    )

def tag(request, slug):
    posts = Post.objects.get_published()\
        .filter(tags__slug=slug)

    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'postt/pages/idx.html',
        {
            'page_obj': page_obj,
        }
    )

def page(request,slug):
    page = (
        Page.objects
        .filter(is_published=True)
        .filter(slug=slug)
        .first()
    )

    return render(
        request,
        'postt/pages/page.html',
        {
            'page': page,
        }
    )


def post(request, slug):
    post = (
        Post.objects.get_published()
        .filter(slug=slug)
        .first()
    )


    return render(
        request,
        'postt/pages/post.html',
        {
            'post': post,
        }
    )

def about(request):

    return render(
        request,
        'postt/pages/about.html',
        {
            # 'page_obj': page_obj,
        }
    )
