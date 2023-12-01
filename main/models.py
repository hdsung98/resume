from django.db import models

class Post(models.Model):
  postname = models.CharField(max_length=50)
  mainphoto = models.ImageField(blank=True, null=True)
  contents = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.postname