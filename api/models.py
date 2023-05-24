from django.db import models

# Create your models here.
class AnnualData(models.Model):
    well = models.CharField(max_length=255, primary_key=True)
    oil = models.IntegerField()
    gas = models.IntegerField()
    brine = models.IntegerField()

    class Meta:
        verbose_name_plural = "Annual Data"
        ordering = ['well']

    def __str__(self):
        return self.well


