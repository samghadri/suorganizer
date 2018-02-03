from django.test import TestCase
from .models import Tag, StartUp
# Create your tests here.

class TagModelTest(TestCase):

    def test_string_representation(self):
        tag = Tag(name='hello')
        # startup = StartUp(name='helloo')
        self.assertEqual(str(tag),tag.name.title())
        # self.assertEqual(str(startup),startup.name)


class StartupModelTest(TestCase):

    def test_string_representation(self):
        startup = StartUp(name='TMT')
        self.assertEqual(str(startup),startup.name)

    def test_ordering(self):
        self.assertEqual(str(StartUp._meta.verbose_name_plural), 'Startups')
