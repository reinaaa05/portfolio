from django import forms

class ContactForm(forms.Form):
    CATEGORIES = (
        ('1', 'お仕事の依頼'),
        ('2', 'サイト内容に関するお問い合わせ'),   
    )

    name = forms.CharField(
        label='お名前', max_length=50,
        required=False, help_text='※任意'    
    )
    emial = forms.EmailField(
        label='ﾒｰﾙｱﾄﾞﾚｽ', required=False, help_text='※任意'
    )
    text = forms.CharField(label='お問い合わせ内容', widget=forms.Textarea)
    category = forms.MultipleChoiceField(label='カテゴリ', choices=CATEGORIES, widget=forms.CheckboxSelectMultiple)
    created_at = forms.DateField(label='日時')