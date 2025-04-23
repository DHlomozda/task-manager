import random
from datetime import datetime

from django.utils.timezone import get_current_timezone, make_aware
from faker import Faker
from task.models import TaskType, Task, Position, Worker


faker = Faker()


def populate_data(num_tasktype=10, num_position=5, num_workers=20, num_task=50):
    for _ in range(num_tasktype):
        TaskType.objects.get_or_create(name=faker.word())

    for _ in range(num_position):
        Position.objects.create(name=faker.job())

    positions = Position.objects.all()
    for _ in range(num_workers):
        Worker.objects.create(
            username=faker.unique.user_name(),
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            email=faker.email(),
            position=random.choice(positions),
            password=faker.password()
        )

    task_types = TaskType.objects.all()
    workers = Worker.objects.all()
    for _ in range(num_task):
        naive_date = faker.future_date()
        aware_datetime = make_aware(datetime.combine(naive_date, datetime.min.time()))
        task = Task.objects.create(
            name=faker.sentence(),
            description=faker.text(),
            deadline=aware_datetime,
            is_completed=faker.boolean(),
            task_type=random.choice(task_types),
        )
        task.assignees.set(random.sample(list(workers), k=random.randint(1, 3)))
        task.save()