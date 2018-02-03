from django.test import TestCase, Client
from .models import Tag, StartUp, NewsLink
# Create your tests here.s

class TagModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Tag.objects.create(name='Big', slug='big')

    def test_name_label(self):
        tag = Tag(name='macbook')
        tag_label = tag._meta.get_field('name').verbose_name
        self.assertEqual(tag_label,'name')


    def test_string_representation(self):
        tag = Tag(name='hello')
        # startup = StartUp(name='helloo')
        self.assertEqual(str(tag),tag.name.title())
        # self.assertEqual(str(startup),startup.name)

    def test_tag_absolute_url(self):
        tag = Tag(slug='macbook')
        self.assertEqual(tag.get_absolute_url(),'/tag/macbook/')

class StartupModelTest(TestCase):

    def test_string_representation(self):
        startup = StartUp(name='TMT')
        self.assertEqual(str(startup),startup.name)


    def test_ordering(self):
        self.assertEqual(str(StartUp._meta.verbose_name_plural), 'Startups')

    def test_founded_date_label(self):
        startup= StartUp(slug='vertex')
        found_label = startup._meta.get_field('founded_date').verbose_name
        self.assertEqual(found_label, 'date founded')

    def test_name_max_length(self):
        startup= StartUp(slug='vertex')
        max_length = startup._meta.get_field('name').max_length
        self.assertEquals(max_length,50)


    def test_get_absolute_url(self):
        startup = StartUp(slug='vertex')
        #This will also fail if the urlconf is not defined.
        self.assertEquals(startup.get_absolute_url(),'/startup/vertex/')

class NewsLinkModelTest(TestCase):
    pass
