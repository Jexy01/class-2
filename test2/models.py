from django.db import models
from test1.models import Post1
class Comment1(models.Model):
    name = models.CharField(max_length=50)
    d = models.ForeignKey(Post1, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name