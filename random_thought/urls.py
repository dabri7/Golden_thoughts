from django.urls import path
from . import views

app_name = 'random_thought'

urlpatterns = [
    path('', views.random, name='random-thought'),
    path('add/', views.add, name='add-thought'),
    path('list/', views.list_view, name='list-thought'),
    path('<int:pk>/', views.detail, name='detail-thought'),
    path('update/<int:pk>/', views.update, name='update-thought'),
    path('delete/<int:pk>/', views.delete, name='delete-thought'),

]
