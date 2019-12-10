from django import forms


class CommentForm(forms.Form):
    visitor = forms.CharField(max_length=20, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '王大明'}), label='訪客名稱')
    email = forms.EmailField(max_length=20, required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'example@email.com'}), label='信箱')
    content = forms.CharField(max_length=200, widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': '棒極了'}), label='評論')
    def clean_content(self):
        content = self.cleaned_data['content']
        if len(content) < 5:
            raise forms.ValidationError('字數不足')
        return content
# form-control
# required參數代表是不是必填

# class LoginForm(forms.Form):
#      #label修改標籤文字，required不寫則預設接受空白內容，attrs添加bootstrap屬性，placeholder設置預設文字
#     username = forms.CharField(label='用戶名',
#                                widget=forms.TextInput(
#                                             attrs={'class':'form-control', 'placeholder':'請輸入用戶名'}))
#      #widget定義標籤內容，這裡將密碼改為密文，attrs添加bootstrap屬性，placeholder設置預設文字
#     password = forms.CharField(label='密碼',
#                                widget=forms.PasswordInput(
#                                             attrs={'class':'form-control', 'placeholder':'請輸入密碼'}))
