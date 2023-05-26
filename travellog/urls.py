from . import views
from django.urls import path

urlpatterns = [
    path('', views.StartPage.as_view(), name='home'),
]
