from django.db import models


class Post(models.Model):
    StatusChoies = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]
    
    title = models.CharField(max_length=127, unique=True)
    slug = models.SlugField(unique=True)
    published_date = models.DateTimeField()
    views = models.PositiveBigIntegerField()
    reading_minute = models.PositiveIntegerField()
    content_markdown = models.TextField()
    content_html = models.TextField()
    tg_link = models.URLField()
    is_published = models.BooleanField(default=False)
    status = models.CharField(choices=StatusChoies, default='draft')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
