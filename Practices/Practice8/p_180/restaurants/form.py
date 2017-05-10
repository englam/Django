#-*- coding: utf-8 -*-
from django import forms

class CommentForm(forms.Form):
    visitor = forms.CharField(max_length=20)
    #email   = forms.EmailField(max_length=20, required=False)
    email = forms.EmailField(max_length=20, required=False, label='E-mail')
    content = forms.CharField(max_length=200, widget=forms.Textarea())

    #自行定義限制條件 跟 錯誤的顯示的訊息
    def clean_content(self):
        content = self.cleaned_data['content']
        if len(content) < 5:
            raise forms.ValidationError('字數不足')
        return (content)