from django.test import TestCase

from .models import Author

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

    def test_date_of_death_label(self):
        author = Author.objects.get(id=Author.objects.all()[0].id)
        field_label = author._meta.get_field('date_of_death').verbose_name
        self.assertEquals(field_label, 'died')

    def test_first_name_max_length(self):
        author = Author.objects.get(id=Author.objects.all()[0].id)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 50)

    def test_object_name_is_last_name_comma_first_name(self):
        author = Author.objects.get(id=Author.objects.all()[0].id)
        expected_object_name = '%s, %s' % (author.last_name, author.first_name)
        self.assertEquals(expected_object_name, str(author))

    def test_get_absolute_url(self):
        author = Author.objects.get(id=Author.objects.all()[0].id)
        number_of_id = Author.objects.all()[0].id
        self.assertEquals(author.get_absolute_url(), '/blog/blogger/%s' % number_of_id)

