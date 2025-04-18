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
    path("tasktypes/", TaskTypeListView.as_view(), name="taskType-list"),
    path("tasktypes/<int:pk>/detail/", TaskTypeDetailView.as_view(), name="taskType-detail"),
    path("tasktypes/create/", TaskTypeCreateView.as_view(), name="taskType-create"),
    path("tasktypes/<int:pk>/update/", TaskTypeUpdateView.as_view(), name="taskType-update"),
    path("tasktypes/<int:pk>/delete/", TaskTypeDeleteView.as_view(), name="taskType-delete"),
    path("position/", PositionListView.as_view(), name="position-list"),
    path("positions/create/", PositionCreateView.as_view(), name="position-create"),
    path("positions/<int:pk>/detail/", PositionDetailView.as_view(), name="position-detail"),
    path("positions/<int:pk>/update/", PositionUpdateView.as_view(), name="position-update"),
    path("positions/<int:pk>/delete/", PositionDeleteView.as_view(), name="position-delete"),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("workers/create/", WorkerCreateView.as_view(), name="worker-create"),
    path("workers/<int:pk>/update/", WorkerUpdateView.as_view(), name="worker-update"),
    path("workers/<int:pk>/detail/", WorkerDetailView.as_view(), name="worker-detail"),
    path("workers/<int:pk>/delete/", WorkerDeleteView.as_view(), name="worker-delete"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/<int:pk>/detail/", TaskDetailView.as_view(), name="task-detail"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("tasks/<int:pk>/complete/", TaskCompleteStatusView.as_view(), name="task-complete")


] + debug_toolbar_urls()

app_name = "task"
