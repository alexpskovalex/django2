from django import forms
from django.db import models
from .models import Comment, Blog
from django.contrib.auth.forms import AuthenticationForm

# from django.utils.translation import ugettext_lazy as _


class CallbackForm(forms.Form):
    name = forms.CharField(label="Ваше имя", max_length=100)
    phone = forms.CharField(
        label="Ваш телефон",
        max_length=20,
        widget=forms.TextInput(attrs={"class": "phone"}),
    )
    gender = forms.ChoiceField(
        label="Ваш пол", choices=[("Мужской", "Мужской"), ("Женский", "Женский")]
    )
    ad = forms.BooleanField(label="Получать рассылку на e-mail?", required=False)
    email = forms.EmailField(label="e-mail", min_length=7)
    message = forms.CharField(
        label="Ваше впечатление", widget=forms.Textarea(attrs={"rows": 12, "cols": 20})
    )


class BootstrapAuthForm(AuthenticationForm):
    username = forms.CharField(
        max_length=254, widget=forms.TextInput({"placeholder": "Имя пользователя"})
    )
    password = forms.CharField(
        label="Пароль", widget=forms.PasswordInput({"placeholder": "Пароль"})
    )


class CommentForm(forms.ModelForm):
    text = forms.CharField(
        widget=forms.Textarea(attrs={"class": "comment_text"}),
    )

    class Meta:
        model = Comment  # используемая модель
        fields = ("text",)  # требуется заполнить только поле text
        labels = {"text": "Комментарий"}  # метка к полю формы text


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ("title", "description", "content", "image")
        labels = {
            "title": "Заголовок",
            "description": "Краткое описание",
            "content": "Полный текст",
            "image": "Картинка",
        }
