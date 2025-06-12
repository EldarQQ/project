from django import forms
from .models import Post,Comment,Profile

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content','category']
        
class CommentPost(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class AvatarUploadFrom(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["avatar"]


