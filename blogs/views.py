from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse

from .models import Blog, Author, BlogComment
from django.contrib.auth import get_user_model

from django.shortcuts import get_object_or_404

class BlogListView(ListView):
    paginate_by = 5
    model = Blog
    context_object_name = 'blog_list'
    template_name = 'blogs/blog_list.html'


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


class BlogCommentCreate(LoginRequiredMixin, CreateView):
    model = BlogComment
    fields = ['description',]

    def get_context_data(self, **kwargs):
        context = super(BlogCommentCreate, self).get_context_data(**kwargs)
        context['blog'] = get_object_or_404(Blog, pk = self.kwargs['pk'])
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.blog = get_object_or_404(Blog, pk = self.kwargs['pk'])
        return super(BlogCommentCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('blog_detail', kwargs={'pk': self.kwargs['pk']})

