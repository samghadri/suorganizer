from django.db import models
from django.core.urlresolvers import reverse
# from blog.models import Post

class Tag(models.Model):
    name = models.CharField(max_length=40, unique=True)
    slug = models.SlugField(max_length=40,
                            unique=True,
                            help_text='A label for URL config')

    def __str__(self):
        return self.name.title()

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('organizer:organizer_tag_detail',
                        kwargs={'slug':self.slug})

    def get_update_url(self):
        return reverse('organizer:organizer_tag_update', kwargs={'slug':self.slug})

    def get_delete_url(self):
        return reverse('organizer:organizer_tag_delete', kwargs={'slug':self.slug})


class StartUp(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(unique=True,
                            help_text='A label for URL config')
    description = models.TextField()
    founded_date = models.DateField('date founded')
    contact = models.EmailField()
    website = models.URLField(max_length=255)
    tags = models.ManyToManyField(Tag)


    def __str__(self):
        return self.name


    class Meta:
        ordering = ['name']
        get_latest_by = 'founded_date'
        verbose_name_plural = "Startups"



    def get_absolute_url(self):
        return reverse('organizer:organizer_startup_detail',
                        kwargs={'slug':self.slug})

    def get_update_url(self):
        return reverse('organizer:organizer_startup_update', kwargs={'slug':self.slug})

    def get_delete_url(self):
        return reverse('organizer:organizer_startup_delete', kwargs={'slug':self.slug})


class NewsLink(models.Model):
    title = models.CharField(max_length=70)
    pub_date = models.DateField('date published')
    link = models.URLField(max_length=255)
    startup = models.ForeignKey(StartUp)


    def __str__(self):
        return '{}:{}'.format(self.startup, self.title)

    class Meta:
        verbose_name = 'news article'
        ordering = ['-pub_date']
        get_latest_by = 'pub_date'


    def get_absolute_url(self):
        return self.startup.get_absolute_url()

    def get_update_url(self):
        return reverse('organizer:organizer_newslink_update', kwargs={'pk':self.pk})

    def get_delete_url(self):
        return reverse('organizer:organizer_newslink_delete', kwargs={'pk':self.pk})
