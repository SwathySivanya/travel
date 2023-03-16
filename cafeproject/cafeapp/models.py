from django.db import models

# Create your models here.
class place(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    des = models.TextField()

    class Meta:
        db_table = "cafeapp_place"

    def __str__(self):
          return self.name

class team(models.Model):
    name = models.CharField(max_length=300)
    img = models.ImageField(upload_to='pics')
    dis = models.TextField()


    class Meta:
        db_table = "cafeapp_team"


    def __str__(self):
          return self.name