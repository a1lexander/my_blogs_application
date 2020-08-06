from django.test import TestCase

from .models import Author, Blog
from django.urls import reverse

class AuthorModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Author.objects.create(first_name='Big', last_name='Bob')

    def test_first_name_label(self):
        # Получение объекта для тестирования
        author = Author.objects.get(id=Author.objects.all()[0].id)
        # Получение метаданных поля для получения необходимых значений
        field_label = author._meta.get_field('first_name').verbose_name
        # Получение метаданных поля для получения необходимых значений
        self.assertEquals(field_label, 'first name')

    def test_last_name_label(self):
        author = Author.objects.get(id=Author.objects.all()[0].id)
        field_label = author._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label, 'last name')

    def test_date_of_birth_label(self):
        author = Author.objects.get(id=Author.objects.all()[0].id)
        field_label = author._meta.get_field('date_of_birth').verbose_name
        self.assertEquals(field_label, 'date of birth')

    def test_date_of_death_label(self):
        author = Author.objects.get(id=Author.objects.all()[0].id)
        field_label = author._meta.get_field('date_of_death').verbose_name
        self.assertEquals(field_label, 'died')

    def test_first_name_max_length(self):
        author = Author.objects.get(id=Author.objects.all()[0].id)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 50)

    def test_last_name_max_length(self):
        author = Author.objects.get(id=Author.objects.all()[0].id)
        max_length = author._meta.get_field('last_name').max_length
        self.assertEquals(max_length, 50)

    def test_object_name_is_last_name_comma_first_name(self):
        author = Author.objects.get(id=Author.objects.all()[0].id)
        expected_object_name = '%s, %s' % (author.last_name, author.first_name)
        self.assertEquals(expected_object_name, str(author))

    def test_get_absolute_url(self):
        author = Author.objects.get(id=Author.objects.all()[0].id)
        number_of_id = Author.objects.all()[0].id
        self.assertEquals(author.get_absolute_url(), '/blog/blogger/%s' % number_of_id)


class BlogModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Blog.objects.create(title='AI', content='About all')

    def test_title_label(self):
        blog = Blog.objects.get(id=Blog.objects.all()[0].id)
        field_label = blog._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_title_max_length(self):
        blog = Blog.objects.get(id=Blog.objects.all()[0].id)
        max_length = blog._meta.get_field('title').max_length
        self.assertEquals(max_length, 200)

    def test_content_label(self):
        blog = Blog.objects.get(id=Blog.objects.all()[0].id)
        field_label = blog._meta.get_field('content').verbose_name
        self.assertEquals(field_label, 'content')

    def test_content_max_length(self):
        blog = Blog.objects.get(id=Blog.objects.all()[0].id)
        max_length = blog._meta.get_field('content').max_length
        self.assertEquals(max_length, 75000)

    def test_object_name_is_title(self):
        blog = Blog.objects.get(id=Blog.objects.all()[0].id)
        expected_object_name = blog.title
        self.assertEquals(expected_object_name, str(blog))

    def test_get_absolute_url(self):
        blog = Blog.objects.get(id=Blog.objects.all()[0].id)
        number_of_id = Blog.objects.all()[0].id
        self.assertEquals(blog.get_absolute_url(), '/blog/%s' % number_of_id)


# Проверка, что действительно отображается по уквзанному URL-адресу + paginate
class BlogListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_blogs = 8
        for blog_num in range(number_of_blogs):
            Blog.objects.create(title='AI %s' % blog_num, content='About all %s' % blog_num)

    def test_view_url_exists_ad_desired_location(self):
        response = self.client.get('/blog/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('blog_list'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('blog_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blogs/blog_list.html')

    def test_pagination_is_five(self):
        response = self.client.get(reverse('blog_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['blog_list']) == 5)

    def test_lists_all_blogs(self):
        response = self.client.get(reverse('blog_list')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertTrue(len(response.context['blog_list']) == 3)

# Тесты отображений к которым имеют доступ только зарегистрированныу пользователи
