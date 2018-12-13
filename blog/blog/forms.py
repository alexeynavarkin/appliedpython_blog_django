from django.forms import ModelForm, HiddenInput
from blog.models import Post, Comment


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ('user',)
        widgets = {
            "post": HiddenInput(),
        }
