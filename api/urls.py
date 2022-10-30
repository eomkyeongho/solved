from django.urls import path

from . import views

app_name = 'solvedapp'
urlpatterns = [
    path('test/', views.ApiUserListLV.as_view(), name='test'),
]
