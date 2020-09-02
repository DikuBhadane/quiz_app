from django.db import models

# Create your models here.

class Quiz(models.Model):
    CHOICES = (
        ("Sachin Tendulkar", "Sachin Tendulkar"),
        ("Virat Kohli", "Virat Kohli"),
        ("Adam Gilchirst", "Adam Gilchirst"),
        ("Jacques kallis", "Jacques kallis"),
    )
    name = models.CharField(max_length=100, blank=True)
    cricker = models.CharField(max_length = 20, choices = CHOICES, default = 'Sachin Tendulkar')
    flag_color = models.CharField(max_length=50, blank=True)

