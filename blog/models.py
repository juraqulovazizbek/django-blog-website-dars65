from django.db import models


class Post(models.Model):
    StatusChoies = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]
    
    title = models.CharField(unique=True, max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    published_date = models.DateTimeField(blank=True, null=True)
    views = models.PositiveBigIntegerField(default=0)
    reading_minute = models.PositiveIntegerField(default=0)
    content_markdown = models.TextField()
    content_html = models.TextField()
    tg_link = models.URLField()
    is_published = models.BooleanField(default=False)
    status = models.CharField(choices=StatusChoies, default='draft')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.pk)
