from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .models import EmailVerification
from django.conf import settings
from .forms import SignUpForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Генерируем и сохраняем токен
            token = 'some_random_token'
            EmailVerification.objects.create(user=user, token=token)

            # Отправляем письмо с ссылкой для подтверждения
            subject = 'Подтверждение регистрации'
            message = f'Пожалуйста, перейдите по ссылке для подтверждения регистрации: http://127.0.0.1:8000/accounts/verify/{token}'
            from_email = settings.EMAIL_HOST_USER
            to_email = user.email
            send_mail(subject, message, from_email, [to_email])

            return redirect('verification_sent')
    else:
        form = SignUpForm()
    return render(request, 'registration/sign_up.html', {'form': form})


def verification_sent(request):
    return render(request, 'registration/verification.html')


def verify(request, token):
    verification = EmailVerification.objects.get(token=token)
    user = verification.user
    user.is_active = True
    user.save()
    verification.delete()
    auth_login(request, user)
    return redirect('/')


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'


@login_required
def user_logout(request):
    logout(request)
    return render(request, 'accounts/logout.html')