from django import forms
from django.forms import formset_factory

class ArticleForm(forms.Form):
    Address = forms.CharField()