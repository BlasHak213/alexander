from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.template.loader import render_to_string

from .models import PostCategory
from .tasks import new_post_notification
from django.conf import settings


# def send_notifications(preview, pk, title, subscribers):
#     html_content = render_to_string(
#         'flatpages/post_created_email.html',
#         {
#             'text': preview,
#             'link': f'{settings.SITE_URL}/newspaper/{pk}'
#         }
#     )
#
#     msg = EmailMultiAlternatives(
#         subject=title,
#         body='',
#         from_email=settings.DEFAULT_FROM_EMAIL,
#         to=subscribers,
#     )
#
#     msg.attach_alternative(html_content, 'text/html')
#     msg.send()
#
#
# @receiver(m2m_changed, sender=PostCategory)
# def notify_about_new_post(sender, instance, **kwargs):
#     if kwargs['action'] == 'post_add':
#         categories = instance.postCategory.all()
#         subscribers:  list[str] = []
#         for category in categories:
#             subscribers += category.subscribers.all()
#
#         subscribers = [s.email for s in subscribers]
#
#         send_notifications(instance.preview(), instance.pk, instance.title, subscribers)


@receiver(m2m_changed, sender=PostCategory)
def new_post_released(sender, instance: list[str], **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.postCategory.all()
        subscribers = []

        for category in categories:
            subscribers += category.subscribers.all()

        subscribers = [s.email for s in subscribers]

        new_post_notification.delay(instance.preview(), instance.pk, instance.title, subscribers)