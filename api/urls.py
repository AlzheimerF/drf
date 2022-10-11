from django.urls import path
from .views import my_api_view, tasklist_view, taskdetail_view, taskcreate_view, taskupdate_view, TasksAPIView, taskdelete_view


urlpatterns = [
    path('', my_api_view),
    path('tasks/', tasklist_view),
    path('task-detail/<int:id>/', taskdetail_view),
    path('task-create/', taskcreate_view),
    path('task-update/<int:id>/', taskupdate_view),
    path('task-delete/<int:id>/', taskdelete_view),
    # path('task-list/', TasksAPIView.as_view()),
    # path('task-list/<int:pk>/', TasksAPIView.as_view()),
]
