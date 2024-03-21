from django.urls import path
from .views import AdList, AdDetail, AdCreate, AdUpdate, AdDelete, AdAdResponse, AdResponsesPersonalList
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', AdList.as_view(), name='ad_list'),
    path('<int:pk>', AdDetail.as_view(), name='ad_detail'),
    path('ad_create/', AdCreate.as_view(), name='ad_create'),
    path('<int:pk>/ad_update', AdUpdate.as_view(), name='ad_update'),
    path('<int:pk>/ad_delete', AdDelete.as_view(), name='ad_delete'),
    path('<int:pk>/ad_response', AdAdResponse.as_view(), name='ad_response'),
    path('responses_list/', AdResponsesPersonalList.as_view(), name='responses_list')

] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)