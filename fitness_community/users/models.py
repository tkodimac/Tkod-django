from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Inherit fields from AbstractUser (username, email, password, etc.)
    is_subscriber = models.BooleanField(default=False)
    # Add any other fields you need for user profiles (e.g., bio, profile picture)