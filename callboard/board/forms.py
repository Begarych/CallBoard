from django import forms

from .models import Post, Response


class AdForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['category', 'title', 'text',]
        widgets = {'author': forms.HiddenInput()}


class UserResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['text',]
        widgets = {'author': forms.HiddenInput()}


class UserResponseAcceptForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = []
        widgets = {'author': forms.HiddenInput()}
