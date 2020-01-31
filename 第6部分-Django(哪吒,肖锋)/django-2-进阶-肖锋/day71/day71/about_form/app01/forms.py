from django import forms
from django.forms import widgets
from app01 import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
import re

def check_name(value):
    if 'alex' in value:
        raise ValidationError('不符合社会主义核心价值观')


# 定义form
class RegForm(forms.Form):
    user = forms.CharField(
        label='用户名',
        required=False,
        min_length=6,
        initial='alexdsb',
        disabled=False,
        validators=[check_name],
        error_messages={
            'min_length': '你的长度太短了，还不到6',
            'required': '不能为空'
        }
    )
    #
    pwd = forms.CharField(
        label='密码',
        min_length=6,
        widget=widgets.PasswordInput()
    )
    re_pwd = forms.CharField(
        label='确认密码',
        min_length=6,
        widget=widgets.PasswordInput()
    )

    #
    # gender = forms.ChoiceField(
    #     choices=((1, '男'), (2, '女'), (3, '不详')),
    #     widget=widgets.CheckboxSelectMultiple()
    # )
    #
    # hobby = forms.ChoiceField(
    #     # choices=((1, '足球'), (2, '篮球'), (3, '双色球')),
    #     choices=models.Hobby.objects.all().values_list('id', 'name'),
    #     widget=widgets.SelectMultiple()
    # )

    phone = forms.CharField(
        label='手机号',
        # validators=[
        #     RegexValidator(r'^1[3-9]\d{9}$', '手机号不正经')
        # ]
    )

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['hobby'].choices = models.Hobby.objects.all().values_list('id', 'name')

    # def clean_phone(self):
    #     value = self.cleaned_data.get('phone')
    #     if re.match(r'^1[3-9]\d{9}$',value):
    #         return value
    #
    #     raise ValidationError('手机号不正经')

    # def clean_re_pwd(self):
    #     pwd = self.cleaned_data.get('pwd')
    #     re_pwd = self.cleaned_data.get('re_pwd')
    #
    #     if pwd == re_pwd:
    #         return re_pwd
    #     raise ValidationError('两次密码不一致')

    def clean(self):
        pwd = self.cleaned_data.get('pwd')
        re_pwd = self.cleaned_data.get('re_pwd')

        if pwd == re_pwd:
            return self.cleaned_data
        self.add_error('re_pwd','两次密码不一致')
        raise ValidationError('两次密码不一致')