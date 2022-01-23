from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import DetailView, ListView, CreateView
from rest_framework import generics

from .models import *
from .forms import *
from .rest_framework import CommentsRest, PostRest


class HomeView(ListView):
    model = Post
    template_name = 'myblog/home.html'
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        context['promo'] = True
        return context


class SinglePostView(DetailView):
    model = Post
    template_name = 'myblog/single.html'
    context_object_name = 'content'

    def get_context_data(self, **kwargs):
        post = get_object_or_404(Post, slug=self.kwargs['slug'])
        post.views += 1
        post.save()

        context = super().get_context_data(**kwargs)
        context['title'] = f"""
        {get_object_or_404(Category, slug=self.kwargs['category']).title} :: 
        {get_object_or_404(Post, slug=self.kwargs['slug']).title}"""
        context['tags'] = Tags.objects.all()
        context['posts'] = Post.objects.all().order_by('-views')
        return context


class CategoryView(ListView):
    model = Post
    template_name = 'myblog/home.html'
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = get_object_or_404(
            Category, slug=self.kwargs['slug'])
        context['promo'] = False
        return context


class TagsView(ListView):
    template_name = 'myblog/home.html'
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = get_object_or_404(Tags, slug=self.kwargs['slug'])
        context['promo'] = False
        return context


class SearchView(ListView):
    template_name = 'myblog/home.html'
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.filter(title__icontains=self.request.GET.get('s'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Search'
        context['promo'] = False
        context['s'] = f"s={self.request.GET.get('s')}&"
        return context


class CommentsRestGetView(generics.ListAPIView):
    serializer_class = CommentsRest

    def get_queryset(self):
        return Comments.objects.filter(slug=self.kwargs['slug'])


class CommentsRestPostView(generics.CreateAPIView):
    serializer_class = CommentsRest


class PostRestGetViews(generics.ListAPIView):
    serializer_class = PostRest
    queryset = Post.objects.all()
