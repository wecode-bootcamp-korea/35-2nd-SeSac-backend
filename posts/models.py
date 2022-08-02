from django.db import models

from core.models  import TimeStampModel
from users.models import User

class Post(TimeStampModel):
    user     = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    location = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True)
    title    = models.CharField(max_length=50)
    content  = models.TextField()
    category = models.ManyToManyField('Category', through='PostCategory')

    class Meta:
        db_table = 'posts'

class Category(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'categories'

class PostCategory(models.Model):
    post     = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        db_table = 'posts_categories'

class Hashtag(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'hashtags'

class PostHashtag(models.Model):
    post    = models.ForeignKey(Post, on_delete=models.CASCADE)
    hashtag = models.ForeignKey(Hashtag, on_delete=models.CASCADE)

    class Meta:
        db_table = 'posts_hashtags'

class Image(models.Model):
    post      = models.ForeignKey(Post, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=255)

    class Meta:
        db_table = 'images'

class Location(models.Model):
    address   = models.CharField(max_length=255)
    latitude  = models.DecimalField(max_digits=10, decimal_places=6)
    longitude = models.DecimalField(max_digits=10, decimal_places=6)

    class Meta:
        db_table = 'locations'
