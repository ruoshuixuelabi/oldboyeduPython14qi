from django import forms
from django.core.validators import ValidationError

class RegForm(forms.Form):
    username = forms.CharField(
        label='用户名',

    )

    password = forms.CharField(
        label='密码',
        widget=forms.widgets.PasswordInput(),
        min_length=8,

    )

    re_password = forms.CharField(
        label='确认密码',
        widget=forms.widgets.PasswordInput(),
        min_length=8,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

    def clean(self):
        pwd = self.cleaned_data.get('password')
        re_pwd = self.cleaned_data.get('re_password')

        if pwd == re_pwd:
            return self.cleaned_data
        self.add_error('re_password', '两次密码不一致')
        raise ValidationError('两次密码不一致')
