from django import forms
from .models import Comment, Video

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
