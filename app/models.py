from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    description = models.TextField()
    release_date = models.CharField(max_length=4)
    imdb_rating = models.FloatField()
    duration = models.FloatField()
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    is_active = models.BooleanField(default=False)