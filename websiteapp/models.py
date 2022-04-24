from django.db import models

# Create your models here.
class product(models.Model):
    name=models.CharField(max_length=20)
    price=models.IntegerField()
    image=models.ImageField(upload_to="img/")
    description=models.TextField()

    def __str__(self):
        return self.name
