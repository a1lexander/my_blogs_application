from django.urls import path
from .views import BlogListView, BloggerListView

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('bloggers/', BloggerListView.as_view(), name='blogger_list'),

]
