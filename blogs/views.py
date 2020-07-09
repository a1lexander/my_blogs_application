from django.views.generic import ListView, DetailView

from .models import Blog, Author

class BlogListView(ListView):
    paginate_by = 5
    model = Blog
    context_object_name = 'blog_list'
    template_name = 'blogs/blog_list.html'

    # def get_queryset(self):
    #     return Blog.objects.filter()[:5]


class BloggerListView(ListView):
    model = Author
    context_object_name = 'blogger_list'
    template_name = 'blogs/blogger_list.html'


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blogs/blog_detail.html'


class BloggerDetailView(DetailView):
    model = Author
    template_name = 'blogs/blogger_detail.html'
