from django.apps import AppConfig


class CabPriceCoefficientAppConfig(AppConfig):
    REDIS_PORT: int = 0
    REDIS_HOST: str = ""
    MYSQL_USER: str = ""
    MYSQL_PASSWORD: str = ""
    MYSQL_HOST: str = ""
    MYSQL_PORT: str = ""
    default_auto_field: str = 'django.db.models.BigAutoField'
    name: str = 'CabPriceCoefficientApp'
