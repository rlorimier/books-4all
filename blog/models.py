from django.db import models
from django.conf import settings
from django.utils import timezone
from cloudinary.models import CloudinaryField


class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="blog_posts")
    title = models.CharField(max_length=200)
    # writtenby = models.CharField(max_length=200)
    featured_image = CloudinaryField('image', default='placeholder')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='blogpost_like', blank=True)

    class Meta:
        ordering = ["-created_date"]

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    
class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    body = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['-published_date']

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.post.title 
