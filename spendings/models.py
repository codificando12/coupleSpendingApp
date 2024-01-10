from django.db import models
from django.utils import timezone
# Create your models here.
class Categories(models.Model):
    #icon = models.ImageField(upload_to='spendings/spending_icons')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=1)
    categoryName = models.CharField(max_length = 100)
    
    def create_initial_spending(self):
        # Crea una nueva instancia de PersonalSpending con spendingAmount = 0
        return PersonalSpending.objects.create(
            user=self.user,
            category=self,
            note="Category created",
            spendingAmount=0,
            spendingDate=timezone.now()
        )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Llama a la función create_initial_spending después de guardar la categoría
        self.create_initial_spending()

    def __str__(self):
        return self.categoryName
    
class PersonalSpending(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    note = models.CharField(max_length = 100)
    spendingAmount = models.FloatField(default = 0)
    spendingDate = models.DateField(default = timezone.now)

    def __str__(self):
        return self.note
