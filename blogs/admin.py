from django.contrib import admin

# Register your models here.
from .models import Blog, Author

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'content')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')


admin.site.register(Blog, BlogAdmin)
admin.site.register(Author, AuthorAdmin)
