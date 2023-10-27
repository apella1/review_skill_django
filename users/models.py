import uuid

from django.db import models


class User(models.Model):
    objects = models.Manager()
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    full_name = f"{first_name} {last_name}"
    email = models.EmailField()
    bio = models.TextField()

    def __str__(self) -> str:
        return str(self.full_name)
