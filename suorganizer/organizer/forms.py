from django import forms
from django.core.exceptions import ValidationError
from .models import Tag


class TagForm(forms.ModelForm):
    # name = forms.CharField(max_length=40)
    # slug = forms.SlugField(max_length=40, help_text='A label for URL config')
    class Meta:
        model = Tag
        fields = "__all__"
                    # ['name', 'slug']
        # exclude = tuple() For the mdoel instances you want to exclude from __all__ forms

    def clean_name(self):
        return self.cleaned_data['name'].lower()

    def clean_slug(self):
        new_slug = (self.cleaned_data['slug'].lower())

        if new_slug == 'create':
            rasie ValidationError('Can not choose create for Slug!')
        return new_slug
