from django.db import models

# Create your models here.
from django.db import models

class ExercisePlan(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    difficulty = models.CharField(max_length=50, choices=[
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ])
    # Add fields for workout days, exercises, sets, reps, etc.
    # You might consider using a JSONField to store exercise data flexibly.
    # Example: exercises = models.JSONField(default=list) 

    def __str__(self):
        return self.name
    
class NutritionPlan(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    dietary_restrictions = models.CharField(max_length=255, blank=True)  # e.g., vegetarian, vegan, gluten-free
    # Add fields for meal plans, calorie targets, macro breakdowns, etc.
    # Similar to ExercisePlan, you might use a JSONField to store meal data.
    # Example: meals = models.JSONField(default=list)

    def __str__(self):
        return self.name