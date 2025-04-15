from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.list_task,name='dashboard'),
    path('addTask/',views.add_task,name='add_task'),
    path('completed/<int:pk>',views.completed_task,name='completed_task'),
    path('delete_task/<int:pk>',views.delete_task,name='delete_task'),
    path('undo_task/<int:pk>',views.undo_task,name='undo_task'),
     path('edit-task/<int:pk>/', views.edit_task, name='edit_task'),
]