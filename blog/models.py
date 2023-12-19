from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField("Название",  max_length=50)
    post = models.TextField("Описание")

    def __str__(self):
        return self.title