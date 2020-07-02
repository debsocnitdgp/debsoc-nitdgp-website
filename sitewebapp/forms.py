from django import forms
from django.forms import ModelForm
from .models import Comments


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['comment_by', 'comment']
