from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /moniter_app/gateway/online
    path('device/<str:device_type>/<str:status>/', views.device, name='device'),
    # ex: /moniter_app/date/2017-05-16
    path('date/<str:date_string>/', views.date, name='date'),
]
