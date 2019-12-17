from django.forms import ModelForm
from django import forms
from django.forms import inlineformset_factory
from .models import StudentSkill,WorkSkill

class s_skillForm(ModelForm):
    class Meta:
        model = StudentSkill
        fields = ("skill",)
        widgets = {
            "skill": forms.TextInput(attrs={'placeholder':'請輸入要新增的技能'}),
        }

class w_skillForm(ModelForm):
    class Meta:
        model = WorkSkill
        fields = ("skill",)
        widgets = {
            "skill": forms.TextInput(attrs={'placeholder':'請輸入要新增的技能'}),
        }