from django import forms
from django.forms import ModelForm
from .models import Comments, Members


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['comment_by', 'comment']

class MemberAddForm(ModelForm):
    class Meta:
        model = Members
        fields = "__all__"
