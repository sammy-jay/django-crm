from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass
class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email

class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    description = models.TextField(max_length=200,null=True, blank=True)
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['-updated_at']

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name