from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.core.exceptions import ValidationError
from .models import Ad, AdResponse


class AdvertisementForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['title', 'text', 'category']
        labels = {'title': 'Заголовок', 'text': 'Текст объявления', 'category': 'Категория'}
        widgets = {'text': CKEditorUploadingWidget()}

    # Не работает с CKEditor
    # def clean(self):
    #     cleaned_data = super().clean()
    #     text = cleaned_data.get("text")
    #     title = cleaned_data.get("title")
    #
    #     if text is None or len(text) > 1000:
    #         raise ValidationError({
    #             "text": "Текст объявления не может быть пустым или превышать более 1000 символов."
    #         })
    #
    #     if title == text or title is None:
    #         raise ValidationError({
    #             'title': 'Заголовок объявления не может совпадать с текстом объявления или быть пустым'
    #         })
    #
    #     return cleaned_data


class ResponseForm(forms.ModelForm):
    class Meta:
        model = AdResponse
        fields = ['text']
        labels = {'text': 'Текст отклика'}