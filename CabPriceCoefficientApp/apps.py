from django.apps import AppConfig


class CabPriceCoefficientAppConfig(AppConfig):
    PORT: int = 6379
    REDIS_HOST: str = "localhost"
    default_auto_field: str = 'django.db.models.BigAutoField'
    name: str = 'CabPriceCoefficientApp'
