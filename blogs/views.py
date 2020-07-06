from django.views.generic import ListView

from .models import Blog, Author

class BlogListView(ListView):
    model = Blog
    template_name = 'blogs/blog_list.html'


class BloggerListView(ListView):
    model = Author
    template_name = 'blogs/blogger_list.html'
