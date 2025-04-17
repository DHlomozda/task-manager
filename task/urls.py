"""
URL configuration for task_services project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls

from task.views import index, TaskTypeListView, PositionListView, TaskTypeUpdateView, TaskTypeDetailView, \
    TaskTypeDeleteView, TaskTypeCreateView, PositionDetailView, PositionUpdateView, PositionDeleteView, \
    PositionCreateView, WorkerListView, WorkerCreateView, WorkerUpdateView, WorkerDetailView, WorkerDeleteView, \
    TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView, TaskCompleteStatusView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="index"),
    path("tasktype/", TaskTypeListView.as_view(), name="taskType-list"),
    path("tasktype/<int:pk>/detail/", TaskTypeDetailView.as_view(), name="taskType-detail"),
    path("tasktype/create/", TaskTypeCreateView.as_view(), name="taskType-create"),
    path("tasktype/<int:pk>/update/", TaskTypeUpdateView.as_view(), name="taskType-update"),
    path("tasktype/<int:pk>/delete/", TaskTypeDeleteView.as_view(), name="taskType-delete"),
    path("position/", PositionListView.as_view(), name="position-list"),
    path("position/create/", PositionCreateView.as_view(), name="position-create"),
    path("position/<int:pk>/detail/", PositionDetailView.as_view(), name="position-detail"),
    path("position/<int:pk>/update/", PositionUpdateView.as_view(), name="position-update"),
    path("position/<int:pk>/delete/", PositionDeleteView.as_view(), name="position-delete"),
    path("worker/", WorkerListView.as_view(), name="worker-list"),
    path("worker/create/", WorkerCreateView.as_view(), name="worker-create"),
    path("worker/<int:pk>/update/", WorkerUpdateView.as_view(), name="worker-update"),
    path("worker/<int:pk>/detail/", WorkerDetailView.as_view(), name="worker-detail"),
    path("worker/<int:pk>/delete/", WorkerDeleteView.as_view(), name="worker-delete"),
    path("task/", TaskListView.as_view(), name="task-list"),
    path("task/<int:pk>/detail/", TaskDetailView.as_view(), name="task-detail"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("task/<int:pk>/complete/", TaskCompleteStatusView.as_view(), name="task-complete")


] + debug_toolbar_urls()

app_name = "task"
