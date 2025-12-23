from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),  # homepage shows student list
    path('add/', views.student_create, name='student_create'),
    path('edit/<int:id>/', views.student_update, name='student_update'),
    path('delete/<int:id>/', views.student_delete, name='student_delete'),
]