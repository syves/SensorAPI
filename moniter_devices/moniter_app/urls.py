from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /polls/5/
    #path('specifics/<int:device_id>/', views.device, name='device'),
    # ex: /polls/5/results/
    #path('<DateTimeField:datetime>', views.date, name='date'),
]
