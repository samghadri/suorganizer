from django import forms
from django.core.exceptions import ValidationError




class TagForm(forms.Form):
    name = forms.CharField(max_length=40)
    slug = forms.SlugField(max_length=40, help_text='A label for URL config')

    def clean_name(self):
        return self.cleaned_data['name'].lower()

    def clean_slug(self):
        new_slug = (self.cleaned_data['slug'].lower())

        if new_slug == 'create':
            rasie ValidationError('Can not choose Create for Slug!')
        return new_slug
