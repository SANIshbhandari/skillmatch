from django.db import models


class SkillGroup(models.Model):
    """Skills in the same group count as 'related' (0.5) in matching."""
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=100, blank=True)
    group = models.ForeignKey(
        SkillGroup, null=True, blank=True,
        on_delete=models.SET_NULL, related_name="skills",
    )
    is_nepal_specific = models.BooleanField(default=False)
    prerequisites = models.ManyToManyField(
        "self", symmetrical=False, blank=True, related_name="unlocks",
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class SkillSynonym(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name="synonyms")
    synonym = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.synonym} -> {self.skill.name}"