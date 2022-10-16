from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='myapp-index'),
    path('predictions/', views.predictions, name='myapp-predictions'),
]
