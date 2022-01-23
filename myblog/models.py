from django.db import models
from django.urls import reverse, reverse_lazy


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Category')
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(viewname='category', kwargs={'slug': self.slug})


class Tags(models.Model):
    title = models.CharField(max_length=50, verbose_name='Tag')
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ['title']

    def get_absolute_url(self):
        return reverse_lazy('tag', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)
    author = models.CharField(max_length=100, verbose_name='Author')
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    photo = models.ImageField(verbose_name='Photo', upload_to='photos/%Y/%m/%d', blank=True)
    views = models.IntegerField(default=0, verbose_name='Count views')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts')
    tags = models.ManyToManyField(Tags, blank=True, related_name='posts')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy(viewname='post', kwargs={'slug': self.slug, 'category': self.category.slug})


class Comments(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    content = models.TextField(verbose_name='Comment')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    slug = models.SlugField(max_length=255, verbose_name='Post')

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['created_at']

    def __str__(self):
        return self.name
