from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    # mapping our user model to the default user model
    user = models.OneToOneField(User, on_delete=models.CASCADE,)

    # adding additional fields to the our user model
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='basic_app/profile_pics', blank=True)

    def __str__(self):
        return self.user.username
