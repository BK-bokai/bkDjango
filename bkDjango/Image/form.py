from django.forms import ModelForm
from django import forms
from django.forms import inlineformset_factory
from .models import Images


class IMGForm(ModelForm):

    publish = forms.fields.ChoiceField(
        label="是否公開",
        initial="checked",
        widget=forms.widgets.CheckboxInput()
    )

    # publish = forms.RegexField(
    #     label="是否公開",
    #     initial="checked",
    #     widget=forms.widgets.CheckboxInput()
    # )

    # gender = forms.CheckboxInput(
    #     choices=((1, "男"), (2, "女"), (3, "保密")),
    #     label="性别",
    #     initial=3,
    #     widget=forms.widgets.RadioSelect()
    # )

    CHOICES=[('select1','select 1'),
         ('select2','select 2')]

    like = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect) 
    FRUIT_CHOICES= [
    ('orange', 'Oranges'),
    ('cantaloupe', 'Cantaloupes'),
    ('mango', 'Mangoes'),
    ('honeydew', 'Honeydews'),
    ]
    favorite_fruit= forms.CharField(label='What is your favorite fruit?', widget=forms.RadioSelect(choices=FRUIT_CHOICES))



    class Meta:
        model = Images
        fields = ("path",)
        widgets = {
            "path": forms.FileInput(),
        #     # "publish": forms.TextInput(attrs={'class': 'form-control', 'placeholder': '台灣熱炒'}),
        }
