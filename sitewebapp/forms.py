from django import forms
from django.forms import ModelForm
from .models import Alumni, Comments, Members,blog


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['comment',]

class MemberAddForm(ModelForm):
    class Meta:
        model = Members
        fields = "__all__"


class blogcform(ModelForm):
    class Meta:
        model=blog
        fields=['title','blog_text','image_url','author']


class alumniform(ModelForm):
    class Meta:
        model=Alumni
        fields="__all__"