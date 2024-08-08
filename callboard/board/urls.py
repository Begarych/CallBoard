from django.urls import path
from .views import AdList, AdDetail, AdCreate, AdUpdate, AdDelete, UserResponseCreate, UserResponseList, UserResponseAccept, UserResponseDelete


urlpatterns = [
   path('ad/', AdList.as_view(), name='ad'),
   path('ad/<int:pk>', AdDetail.as_view(), name='ad_detail'),
   path('ad/create/', AdCreate.as_view(), name='ad_create'),
   path('ad/<int:pk>/edit/', AdUpdate.as_view(), name='ad_update'),
   path('ad/<int:pk>/delete/', AdDelete.as_view(), name='ad_delete'),
   path('response/', UserResponseList.as_view(), name='response'),
   path('<int:pk>/response/create/', UserResponseCreate.as_view(), name='response_create'),
   path('response/<int:pk>/delete/', UserResponseDelete.as_view(), name='response_delete'),
   path('response/<int:pk>/accept/', UserResponseAccept.as_view(), name='response_accept'),
]