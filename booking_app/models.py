from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

APPARTMENT_CHOICES = (
    ("Matea", "Matea-4pax"),
    ("Martina", "Martina-6pax"),
    ("Antonio", "Antonio-4pax"),
    )

TIME_CHOICES = (
    ("3 PM", "3 PM"),
    ("3:30 PM", "3:30 PM"),
    ("4 PM", "4 PM"),
    ("4:30 PM", "4:30 PM"),
    ("5 PM", "5 PM"),
    ("5:30 PM", "5:30 PM"),
    ("6 PM", "6 PM"),
    ("6:30 PM", "6:30 PM"),
    ("7 PM", "7 PM"),
    ("7:30 PM", "7:30 PM"),
)