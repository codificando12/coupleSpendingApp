from django.db import models

# Create your models here.
class PersonalSpending(models.Model):
    # icon =models.CharField(max_length=100)
    category = models.CharField(max_length = 100)
    spending = models.CharField(max_length = 100)
    spendingAmount = models.FloatField()

    def __str__(self):
        return self.spending
