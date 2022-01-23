from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/<str:slug>', CategoryView.as_view(), name='category'),
    path('tags/<str:slug>', TagsView.as_view(), name='tag'),
    path('category/<str:category>/post/<str:slug>',
         SinglePostView.as_view(), name='post'),
    path('search/', SearchView.as_view(), name='search'),
    path('rest/comments/get/<str:slug>', CommentsRestGetView.as_view()),
    path('rest/comments/post/<str:slug>', CommentsRestPostView.as_view(),),
    path('rest/posts/get/', PostRestGetViews.as_view(),),
]
