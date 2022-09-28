from django.db import models


class ThresholdWeightModel(models.Model):
    requests_threshold = models.IntegerField(null=False, primary_key=True)
    price_coefficient = models.FloatField(null=False)

    def __str__(self):
        return f'{self.requests_threshold} - {self.price_coefficient}'
