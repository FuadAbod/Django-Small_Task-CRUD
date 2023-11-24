from django.db import models

class Cake(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    comment = models.CharField(max_length=200)
    imageUrl = models.URLField()
    yumFactor = models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])

