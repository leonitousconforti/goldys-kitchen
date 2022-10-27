from django.urls import path

from . import views

appname = 'kitchen'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:recepie_id>/', views.detail, name='detail'),
]