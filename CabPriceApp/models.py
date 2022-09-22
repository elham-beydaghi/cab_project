from django.db import models


class PriceWeightModel(models.Model):
    requests_threshold = models.IntegerField(max_length=15, null=False, primary_key=True)
    price_coefficient = models.IntegerField(max_length=5, null=False)

    def __str__(self):
        return f'{self.requests_threshold} - {self.price_coefficient}'
