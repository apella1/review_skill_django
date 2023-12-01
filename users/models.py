import uuid

from django.db import models


class User(models.Model):
    objects = models.Manager()
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField()
    avatar = models.ImageField()

    def __str__(self) -> str:
        return str(self.first_name + " " + self.last_name)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Task(models.Model):
    objects = models.Manager()
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=False)
    media = models.ImageField()
