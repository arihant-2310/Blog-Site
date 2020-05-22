from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateField(auto_now_add=True)

    #it defines how the model should be returned in shell
    def __str__(self):
        return self.title
    #to return only first 50 characters
    def snippet(self):
        return self.body[:50] + '...'
