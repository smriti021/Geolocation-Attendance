from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('mark/', views.mark_attendance, name='mark_attendance'),
    path('success/', views.attendance_success, name='attendance_success'),
    path('view/', views.view_attendance, name='view_attendance'),
]
