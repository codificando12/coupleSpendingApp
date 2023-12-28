from django.db import models
from django.utils import timezone
# Create your models here.
class Categories(models.Model):
    #icon = models.ImageField(upload_to='spendings/spending_icons')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=1)
    categoryName = models.CharField(max_length = 100)

    def __str__(self):
        return self.categoryName
    
class PersonalSpending(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    spending = models.CharField(max_length = 100)
    spendingAmount = models.FloatField()
    spendingDate = models.DateField(default = timezone.now)

    def __str__(self):
        return self.spending
