from django.test import TestCase
from django.utils.timezone import now
from task.models import Task, TaskType, Worker, Position


class TaskModelTest(TestCase):
    def setUp(self):
        self.position = Position.objects.create(name="Developer")
        self.worker = Worker.objects.create_user(
            username="john_doe",
            password="testpassword123",
            first_name="John",
            last_name="Doe",
            position=self.position,
        )
        self.task_type = TaskType.objects.create(name="Bug Fix")
        self.task = Task.objects.create(
            name="Fix critical bug",
            description="Fix the critical bug in the payment system",
            deadline=now(),
            priority=Task.Priority.URGENT,
            task_type=self.task_type,
        )
        self.task.assignees.add(self.worker)

    def test_task_creation(self):
        self.assertEqual(self.task.name, "Fix critical bug")
        self.assertEqual(self.task.priority, Task.Priority.URGENT)
        self.assertIn(self.worker, self.task.assignees.all())

    def test_task_string_representation(self):
        self.assertEqual(
            str(self.task),
            "Fix critical bug: Fix the critical bug in the payment system",
        )

    def test_task_type_representation(self):
        self.assertEqual(str(self.task_type), "Bug Fix")

    def test_worker_representation(self):
        self.assertEqual(str(self.worker), "John Doe")

    def test_task_search_by_name(self):
        results = Task.objects.filter(name__icontains="Fix")
        self.assertIn(self.task, results)

    def test_task_search_by_priority(self):
        results = Task.objects.filter(priority=Task.Priority.URGENT)
        self.assertIn(self.task, results)


class WorkerModelTest(TestCase):
    def setUp(self):
        self.position = Position.objects.create(name="Manager")
        self.worker = Worker.objects.create_user(
            username="jane_doe",
            password="securepassword",
            first_name="Jane",
            last_name="Doe",
            position=self.position,
        )

    def test_worker_creation(self):
        self.assertEqual(self.worker.position.name, "Manager")

    def test_worker_absolute_url(self):
        self.assertEqual(self.worker.get_absolute_url(), f"/worker/{self.worker.pk}/detail/")
