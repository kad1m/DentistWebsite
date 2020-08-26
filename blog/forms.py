from django import forms
from .models import Comment


class PostShareViaEmail(forms.Form):
    name = forms.CharField(max_length=25)
    to = forms.EmailField()

    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control mb-30', 'placeholder': 'Your name', 'name': 'message-name'}))
    to = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control mb-30', 'placeholder': 'Your Email', 'name': 'message-email'}))


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-30', 'placeholder': 'Your name', 'name': 'message-name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control mb-30', 'placeholder': 'Your Email', 'name': 'message-email'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control mb-30', 'placeholder': 'Your Text', 'name': 'message'}))
