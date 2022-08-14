from django import forms
from .models import Comment, Reply

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ['post', 'id']

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = '__all__'
        exclude = ['comment', 'id']

class SearchFrom(forms.Form):
    title = forms.CharField(max_length=200)