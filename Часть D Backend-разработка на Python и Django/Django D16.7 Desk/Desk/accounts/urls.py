from django.urls import path
from . import views
from .views import CustomLoginView
from django.contrib.auth.views import auth_logout


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('verification_sent/', views.verification_sent, name='verification_sent'),
    path('verify/<str:token>/', views.verify, name='verify'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout')
]