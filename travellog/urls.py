from . import views
from django.urls import path

urlpatterns = [
    path('', views.LogentryList.as_view(), name='home'),
]
