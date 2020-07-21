from django.views.generic import TemplateView

from blogs.models import Blog

class HomePageView(TemplateView):
    template_name = 'home.html'



