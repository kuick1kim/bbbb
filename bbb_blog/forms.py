# forms.py
from django import forms
from .models import Post

class RemovePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = []  # 필요한 경우 추가 필드 지정



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)
