from django.forms import ModelForm
from django import forms
from django.forms import inlineformset_factory
from .models import Store,Food

class InlineStoreForm(ModelForm):
    class Meta:
        model = Store
        fields = ("boss", "store_name", "phone", "address")
        widgets = {
            "boss": forms.TextInput(attrs={'class':'form-control','placeholder':'王曉明'}),
            "store_name":forms.TextInput(attrs={'class':'form-control','placeholder':'台灣熱炒'}),
            "phone":forms.TextInput(attrs={'class':'form-control','placeholder':'0912345678'}),
            "address":forms.TextInput(attrs={'class':'form-control','placeholder':'台北市和平東路25號'})
        }


InlineFoodFormSet = inlineformset_factory(Store, Food, fields=('food_name','price'),max_num=10,extra=1,
                                        can_delete=False,widgets={
    'food_name': forms.TextInput(attrs={'class':'form-control','placeholder':'薑絲炒大腸'}),
    'price'    : forms.TextInput(attrs={'class':'form-control','placeholder':'100'})
})