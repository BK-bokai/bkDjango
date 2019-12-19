from django.forms import ModelForm
from django import forms
from django.forms import inlineformset_factory
from .models import Messages, Replies


class MsgForm(ModelForm):

    class Meta:
        model = Messages
        fields = ("body",)
        widgets = {
            "body": forms.Textarea(attrs={'class': 'materialize-textarea', 'id': 'autocomplete-input', 'name': 'msg-content'})
        }
        labels = {
            "body": "你想講些什麼?",
        }


class ReplyForm(ModelForm):

    class Meta:
        model = Replies
        fields = ("body",)
        widgets = {
            "body": forms.Textarea(attrs={'class': 'materialize-textarea', 'id': 'autocomplete-input', 'name': 'msg-content'})
        }
        labels = {
            "body": "請輸入回覆內容",
        }
