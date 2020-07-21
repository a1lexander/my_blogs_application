import uuid # new
from django.contrib.auth import get_user_model # new
from django.db import models
from django.urls import reverse # new

class Blog(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    content = models.TextField(max_length=75000)
    published = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        verbose_name_plural = 'Blogs'
        verbose_name = 'Blog'
        ordering = ['-published']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail', args=[str(self.id)])


class Author(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)

    def get_absolute_url(self):
        return reverse('author_detail', args=[str(self.id)])


class BlogComment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000,
                               help_text='Leave a comment in language (e.g. English, French, Japanese, Russian, Ukrainian etc.)')
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
    post_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['post_date']

    def __str__(self):
        len_title=75
        if len(self.comment)>len_title:
            titlestring=self.comment[:len_title] + '...'
        else:
            titlestring=self.comment
        return titlestring
