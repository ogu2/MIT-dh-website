from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class MemeberProfile(User):
	fb_username=models.CharField(max_length=50)