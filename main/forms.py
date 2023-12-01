from django import forms
from django.core.exceptions import ValidationError
from .models import Post

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ['postname', 'contents', 'mainphoto']

  def clean_postname(self):
    postname = self.cleaned_data.get('postname')
    if len(postname) < 1:
      raise ValidationError("제목에는 최소한 한 글자 이상의 문자가 포함되어야 합니다.")
    return postname