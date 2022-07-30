from django.urls import path

from . import views

app_name = 'solvedapp'
urlpatterns = [
    path('test/', views.ApiTodoLV.as_view(), name='test'),
]
