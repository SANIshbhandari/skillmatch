from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        SEEKER = 'seeker', 'Job seeker'
        RECRUITER = 'recruiter', 'Recruiter'
        ADMIN = 'admin', 'Admin'

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.SEEKER,
    )

def save(self, *args, **kwargs):
        if self.is_superuser:
            self.role = "admin"
        super().save(*args, **kwargs)
