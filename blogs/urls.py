from django.urls import path
from .views import BlogListView, BloggerListView, BlogDetailView, BloggerDetailView, \
    BlogCommentCreate

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('bloggers/', BloggerListView.as_view(), name='blogger_list'),
    path('<uuid:pk>', BlogDetailView.as_view(), name='blog_detail'),
    path('blogger/<uuid:pk>', BloggerDetailView.as_view(), name='author_detail'),
    path('blog/<uuid:pk>/comment/', BlogCommentCreate.as_view(), name='blog_comment'),
]
