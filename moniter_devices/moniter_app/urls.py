from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /moniter_app/device/'bb10684d'/results
    path('device/<str:device_id>/<str:status>/', views.device, name='device'),
    # ex: /moniter_app/15/results/
    path('date/<int:datetime>/', views.date, name='date'),
]
