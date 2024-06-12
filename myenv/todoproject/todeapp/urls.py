from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('update_task/<str:Id>',views.updatetask,name='update_task'),
    path('delete_task/<str:Id>',views.deletetask,name='delete_task'),
]
