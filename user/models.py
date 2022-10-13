from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.
class UserModel(AbstractUser):
    class Meta:
        db_table = "db_user"
        
    username = models.CharField(max_length=15, unique=True, null=True)
    profile_image = models.ImageField(default="default_profile_pic.jpg", upload_to="profile_pics")
    intro = models.CharField(max_length=60, blank=True)
    follow = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = 'followee')