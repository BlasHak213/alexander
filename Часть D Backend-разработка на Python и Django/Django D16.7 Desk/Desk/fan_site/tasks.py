import datetime
from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from .models import Ad, User
from django.conf import settings


@shared_task
def send_weekly_newsletter():
    day = datetime.datetime.now()
    last_week = day - datetime.timedelta(days=7)
    last_week_ads = Ad.objects.filter(date_creation__gte=last_week).order_by('date_creation')

    html_content = render_to_string(
        template_name='daily_ad.html',
        context={
            'link': settings.SITE_URL,
            'ads': last_week_ads
        }
    )

    recipients = list(User.objects.values_list('email', flat=True))

    msg = EmailMultiAlternatives(subject='Объявления за неделю:', body='', from_email=settings.DEFAULT_FROM_EMAIL,
                                 to=recipients)
    msg.attach_alternative(html_content, 'text/html')
    msg.send()