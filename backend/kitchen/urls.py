from django.urls import path

from . import views

appname = 'kitchen'
urlpatterns = [
    path('', views.index, name='index'),
    path('recepies/<str:ing_list>', views.recepies, name='recepies'),
    path('<int:recepie_id>/', views.detail, name='detail'),
]
