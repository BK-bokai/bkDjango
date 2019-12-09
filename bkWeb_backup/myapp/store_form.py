from django import forms


class StoreForm(forms.Form):
    boss = forms.CharField(max_length=20,label='負責人',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'王曉明'}))
    store_name = forms.CharField(max_length=10,label='店名',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'台灣熱炒'}))
    phone = forms.CharField(max_length=10,label='電話號碼',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'0912345678'}))
    email = forms.EmailField
    address = forms.CharField(max_length=100,label='地址',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'台北市和平東路25號'}))


class FoodForm(forms.Form):
    food_name = forms.CharField(max_length=30,label='食物',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'薑絲炒大腸'}))
    price = forms.DecimalField(max_digits=3, decimal_places=0,label='價格',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'100'}))
