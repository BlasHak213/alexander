from django import forms
from .models import Post
from django.core.exceptions import ValidationError


class NewsForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'author',
            # 'categoryType',
            'postCategory',
            'title',
            'text',

        ]

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get("text")
        title = cleaned_data.get("title")

        if text is not None and len(text) > 100:
            raise ValidationError({
                "text": "Текст поста не может быть более 100 символов."
            })

        if title == text:
            raise ValidationError({
                'title': 'Название поста не может совпадать с текстом поста'
            })

        return cleaned_data

    # def clean_title(self):
    #     title = self.cleaned_data['title']
    #     if title[0].islower():
    #         raise ValidationError({
    #             'title': 'Заголовок должен начинаться с заглавной буквы'
    #         })
    #
    # def clean_text(self):
    #     text = self.cleaned_data['text']
    #     if text[0].islower():
    #         raise ValidationError({
    #             'text': 'Текст поста должен начинаться с заглавной буквы'
    #         })


