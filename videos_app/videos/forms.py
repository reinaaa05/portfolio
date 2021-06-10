from django import forms
from .models import Comment, Video, Category

class VideoCreate(forms.ModelForm):
    class Mata:
      model = Video
      exclude = ('writer',)

class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
          'text' : forms.Textarea(attrs={'class': 'textarea'})
        }

class VideoSearchForm(forms.Form):
    key_word = forms.CharField(
      label='キーワード', required=False,
      widget=forms.TextInput(attrs={'class': 'input'})
    )
