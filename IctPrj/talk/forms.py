from django import forms
from .models import talk

class PostForm(forms.ModelForm):
    class Meta:
        model = talk
        fields = ['content']