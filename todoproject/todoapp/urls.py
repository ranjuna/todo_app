from django.urls import path
from . import views
urlpatterns=[path('',views.task_view,name='task_view'),
              path('delete/<int:taskid>/',views.delete,name='delete'),
                path('update/<int:id>/',views.update,name='update'),
             path('viewtask/',views.TaskListView.as_view(),name='viewtask'),
             path('viewdetail/<int:pk>/',views.TaskDetailView.as_view(),name='viewdetail'),
            path('viewupdate/<int:pk>/',views.TaskUpdateView.as_view(),name='viewupdate'),
            path('viewdelete/<int:pk>/',views.TaskDeleteView.as_view(),name='viewdelete')
             ]