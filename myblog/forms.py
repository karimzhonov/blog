from django import forms

from .models import Comments


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['name', 'content', 'slug']
        labels = {
            'name': '',
            'content': '',
            'slug': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Name",
                'style': 'padding: 20px; margin-bottom: 10px'
            }),
            'content': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Comment",
                'style': 'padding: 20px; margin-bottom: 10px'
            }),
            'slug': forms.TextInput(attrs={
                'id': 'slug_input',
                'style': 'display: none;'
            })
        }


class SubscriptionForm(forms.Form):
    search = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            'placeholder': 'Search for items',
        }))

