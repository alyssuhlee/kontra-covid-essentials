from django import forms
from .models import Post

class Post(forms.Post):
    class Meta(object):
        model = Post
        fields = ("name", "email", "phone", "query")