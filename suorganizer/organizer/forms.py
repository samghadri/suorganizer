from django import forms
from django.core.exceptions import ValidationError
from .models import Tag, NewsLink, StartUp



class NewsLinkForm(forms.ModelForm):
    class Meta:
        model = NewsLink
        fields = '__all__'


class SlugCleanMixin:

    def clean_slug(self):
        new_slug =(self.cleaned_data['slug'].lower())
        if new_slug == 'create':
            raise ValidationError('The Slug can not be create!!')
        return new_slug



class StartUpForm(SlugCleanMixin, forms.ModelForm):
    class Meta:
        model = StartUp
        fields = '__all__'



class TagForm(SlugCleanMixin, forms.ModelForm):
    # name = forms.CharField(max_length=40)
    # slug = forms.SlugField(max_length=40, help_text='A label for URL config')
    class Meta:
        model = Tag
        fields = "__all__"
                    # ['name', 'slug']
        # exclude = tuple() For the mdoel instances you want to exclude from __all__ forms

    def clean_name(self):
        return self.cleaned_data['name'].lower()
