from django.forms import ModelForm
from django import forms
from django.forms import inlineformset_factory
from .models import Store, Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        # fields = "__all__"
        fields = ("visitor", "email", "content", )

        widgets = {
            "visitor": forms.TextInput(attrs={'class': 'form-control', 'placeholder': '王曉明'}),
            "email": forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}),
            "content": forms.Textarea(attrs={'class': 'form-control'}),

            # "address":forms.TextInput(attrs={'class':'form-control','placeholder':'地址'})
        }

        labels = {
            "visitor": "訪問者",
            "email"  : "信箱",
            "content": "評論"
        }
