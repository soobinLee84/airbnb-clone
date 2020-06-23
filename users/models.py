from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):

    """ Custome User Model """

    GENDER_FEMAIL = "female"
    GENDER_MALE = "male"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_FEMAIL, "female"),
        (GENDER_MALE, "male"),
        (GENDER_OTHER, "other"),
    )

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"

    LANGUAGE_CHOICES = ((LANGUAGE_ENGLISH, "english"), (LANGUAGE_KOREAN, "korean"))

    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, null=True)
    bio = models.TextField(default="", blank=True)
    birthdate = models.DateField(null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2)
