from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Genre(models.Model):
    genre_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,unique=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=False,null=True,blank=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,related_name='created_genre')
    updated_by = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,related_name='updated_genre') 
    def __str__(self):
        return self.name


class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    description = models.TextField()
    release_date = models.CharField(max_length=4)
    imdb_rating = models.FloatField()
    duration = models.FloatField()
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=False,null=True,blank=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,related_name='created_movies')  # Related_name ~> as we can see user model is used before and both the models are refering to the same user model so  in order to prevent clash we have passed a unique name to both
    updated_by = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,related_name='updated_movies')  # Related_name ~> as we can see user model is used before and both the models are refering to the same user model so  in order to prevent clash we have passed a unique name to both
    genre = models.ForeignKey(Genre,on_delete=models.SET_NULL,null=True,blank=True)
