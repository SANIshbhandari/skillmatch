from django.db import models
from django.conf import settings

from skills.models import Skill


class SeekerProfile(models.Model):
    class EducationLevel(models.TextChoices):
        HIGH_SCHOOL = 'high_school', 'High school'
        DIPLOMA = 'diploma', 'Diploma'
        BACHELORS = 'bachelors', "Bachelor's degree"
        MASTERS = 'masters', "Master's degree"
        DOCTORATE = 'doctorate', 'Doctorate'

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='seeker_profile',
    )
    education_level = models.CharField(
        max_length=20,
        choices=EducationLevel.choices,
        blank=True,
    )
    years_experience = models.PositiveSmallIntegerField(default=0)
    preferences = models.TextField(blank=True)
    skills = models.ManyToManyField(Skill, blank=True, related_name='seekers')

    def __str__(self):
        return f'{self.user.username} seeker profile'


class CompanyProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='company_profile',
    )
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    website = models.URLField(blank=True)
    location = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.name
