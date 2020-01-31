from django import forms
from crm import models
from django.core.exceptions import ValidationError


# 注册form
class RegForm(forms.ModelForm):
    password = forms.CharField(
        label='密码',
        widget=forms.widgets.PasswordInput(),
        min_length=6,
        error_messages={'min_length':'最小长度为6'}
    )
    re_password = forms.CharField(
        label='确认密码',
        widget=forms.widgets.PasswordInput()
    )
    
    class Meta:
        model = models.UserProfile
        # fields = '__all__'   # 所有字段
        fields = ['username', 'password', 're_password', 'name', 'department']  # 指定字段
        # exclude = ['']
        widgets = {
            'username': forms.widgets.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.widgets.PasswordInput,
        }
        
        labels = {
            'username': '用户名',
            'password': '密码',
            'name': '姓名',
            'department': '部门',
        }
        
        error_messages = {
            'password': {
                'required': '密码不能为空',
            }
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for filed in self.fields.values():
            filed.widget.attrs.update({'class': 'form-control'})
    
    def clean(self):
        pwd = self.cleaned_data.get('password')
        re_pwd = self.cleaned_data.get('re_password')
        if pwd == re_pwd:
            return self.cleaned_data
        self.add_error('re_password', '两次密码不一致')
        raise ValidationError('两次密码不一致')
