from django.shortcuts import get_object_or_404, render
from django.utils import timezone

# pyrefly: ignore[missing-import]
from .models import Category, Post


def get_published_posts():
    """Возвращает QuerySet опубликованных постов."""
    return Post.objects.select_related(
        'author', 'location', 'category'
    ).filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True,
    )


def index(request):
    """Главная страница — пять последних публикаций."""
    template = 'blog/index.html'
    post_list = get_published_posts()[:5]
    context = {'post_list': post_list}
    return render(request, template, context)


def post_detail(request, post_id):
    """Страница отдельной публикации."""
    template = 'blog/detail.html'
    post = get_object_or_404(
        get_published_posts(),
        pk=post_id,
    )
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    """Страница категории — все публикации выбранной категории."""
    template = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True,
    )
    post_list = get_published_posts().filter(category=category)
    context = {'category': category, 'post_list': post_list}
    return render(request, template, context)