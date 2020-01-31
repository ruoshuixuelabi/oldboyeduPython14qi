# -*- coding: utf-8 -*-
# __author__ = "maple"

from django import forms

from ckeditor.widgets import CKEditorWidget

from web import models


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        fields = "__all__"
        model = models.Comment
