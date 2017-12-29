from django.db import models
from django.utils.text import slugify
from organizer.models import Tag, StartUp


class Post(models.Model):

    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50,
                            unique_for_month='pub_date',
                            help_text = 'A label for URL config')
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name='blog_posts')
    startups = models.ManyToManyField(StartUp, related_name='blog_posts')


    def __str__(self):
        return '{} on {}'.format(
                    self.title,
                    self.pub_date.strftime('%y-%m-%d'))

    class Meta:
        verbose_name = 'blog posts'
        ordering = ['-pub_date', 'title']
        get_latest_by = 'pub_date'
