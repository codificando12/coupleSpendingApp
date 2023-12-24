from django.db import models
from django.utils import timezone
# Create your models here.
class PersonalSpendingCategories(models.Model):
    icon = models.ImageField(upload_to='spendings/spending_icons')
    category = models.CharField(max_length = 100)
    spendingNote = models.CharField(max_length = 100, default=' ')
    spendingDate = models.DateField(default=timezone.now)

    def __str__(self):
        return self.category
