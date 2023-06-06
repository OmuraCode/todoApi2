from django.urls import path
from .views import task_create_list_view, task_detail_view, TaskListCreateAPIView, TaskDetailAPIView

urlpatterns = [
    path('tasks/', task_create_list_view), #GET/POST
    path('tasks/<int:pk>/', task_detail_view), #GET /PUT PATCH/ DELETE

    path('class/tasks/', TaskListCreateAPIView.as_view()),
    path('class/tasks/<int:pk>/', TaskDetailAPIView.as_view()),
]


#127.0.0.1:8000/api/v1/tasks/ -> GET/POST task_create_list_view
#127.0.0.1:8000/api/v1/tasks/id/--> GET?PUT PSTCH DELETE task_detail_view