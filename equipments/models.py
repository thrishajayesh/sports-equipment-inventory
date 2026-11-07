from django.db import models

class Equipment(models.Model):
    item_name = models.CharField(max_length=100)
    sport = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.item_name} - {self.sport}"