from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class CustomUser(User):
    GENDER_CHOICES = (
        ('M', 'M'),
        ('F', 'F'),
        ('IT', 'IT'),
    )
    age = models.PositiveIntegerField(validators=[MinValueValidator(13), MaxValueValidator(30)])
    phone_number = models.CharField(max_length=13, default='+996')
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES)
