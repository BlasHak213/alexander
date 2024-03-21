from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse


class Ad(models.Model):
    title = models.CharField(max_length=64, unique=True)
    text = RichTextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    upload = models.FileField(upload_to='uploads/')

    def __str__(self):
        return f'{self.category} : {self.title} - {self.text}'

    def get_absolute_url(self):
        return reverse('ad_detail', kwargs={'pk':  self.pk})


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class AdResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    ad = models.ForeignKey('Ad', on_delete=models.CASCADE, related_name='responses')
    date_creation = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return f'Response by {self.user.username} on {self.ad.title}'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
