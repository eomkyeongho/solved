from django.urls import path

from . import views

app_name = 'solvedapp'
urlpatterns = [
    path('vonly/', views.SolvedappVueOnlyTV.as_view(), name='vonly'),

    path('create/', views.TodoCV.as_view(), name='create'),
    path('list/', views.TodoLV.as_view(), name='list'),
    path('<int:pk>/delete', views.TodoDelV.as_view(), name='delete'), # <int:pk> 인트로 변환해서 view에 넘겨줌
]
