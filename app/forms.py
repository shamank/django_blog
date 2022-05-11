from django.forms import ModelForm, Textarea
from .models import Comment

class CommentForm(ModelForm):
    class Meta:
        model = Comment 
        fields = ['content']
        widgets = {
            'content': Textarea(attrs={'placeholder': 'Ваш комментарий...', 'rows': 5}),
        }