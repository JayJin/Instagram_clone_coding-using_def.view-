from django.db import models
from user.models import UserModel

# Create your models here.
class PostModel(models.Model):
    class Meta:
        db_table = 'db_post'
    
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="post_pics")