from django.db import models

# Create your models here.
from django.db import models

class SubscriptionPlan(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # Add fields for features included in the plan (e.g., access_to_exercise_plans, access_to_nutrition_plans)
    
    def __str__(self):
        return self.name