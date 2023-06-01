from django.urls import path, include
from todo import views

urlpatterns = [
    path('', views.add, name='add'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:taskid>/', views.update, name='update'),
    path('clsbaedviewhome/', views.TasklistView.as_view(), name='clsbaedviewhome'),
    path('clsbaeddetailview/<int:pk>/', views.TaskDetailview.as_view(), name='clsbaeddetailview'),
    path('clsbasedUpdateview/<int:pk>/', views.TaskUpdateview.as_view(), name='clsbasedUpdateview'),
    path('clsbasedDeleteview/<int:pk>/', views.TaskUpdateview.as_view(), name='clsbasedDeleteview'),
    # path('details', views.details, name='details'),

]
