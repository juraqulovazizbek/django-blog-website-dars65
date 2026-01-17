from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views import View
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.text import slugify

from .forms import BlogCreateForm, BlogSearchForm
from .models import Post


class HomeView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        posts = Post.objects.all()
        return render(request, 'home.html', {'posts': posts})


class BlogsView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        if request.GET:
            form = BlogSearchForm(request.GET)
            if form.is_valid():
                search = form.cleaned_data['search']

                result = Post.objects.filter(title__icontains=search)

                return render(request, 'blog.html', {'posts': result, 'search': search})

        return render(request, 'blog.html', {'posts': Post.objects.order_by('published_date')})


class BlogDetailView(View):
    def get(self, request: HttpRequest, slug: str) -> HttpResponse:
        try:
            post = Post.objects.get(slug=slug)
            return render(request, 'blog_detail.html', {'post': post})
        except Post.DoesNotExist:
            return render(request, 'blog.html', {'posts': Post.objects.all(), 'error': f'{slug} is not found.'})


class BlogCreateView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        form = BlogCreateForm()
        return render(request, 'blog_create.html', {'form': form})

    def post(self, request: HttpRequest) -> HttpResponse:
        form = BlogCreateForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            post = Post(
                title=data['title'],
                slug=slugify(data['title']),
                reading_minute=data['reading_minute'],
                content_markdown=data['content_markdown'],
                content_html=data['content_html'],
                tg_link=data['tg_link'],
            )
            post.save()

            return redirect(reverse('blogs'))
        
        return render(request, 'blog_create.html', {'form': form})
