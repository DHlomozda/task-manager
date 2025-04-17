from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from task.models import TaskType, Task, Worker, Position

# Register your models here.

admin.site.register(TaskType)
admin.site.register(Task)

admin.site.register(Position)


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("position", )
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("position", )}), )
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "position",
                    )
                },
            ),
        )
    )
