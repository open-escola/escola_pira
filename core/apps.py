from django.apps import AppConfig
from django.core.serializers import register_serializer


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        register_serializer('yml', 'django.core.serializers.pyyaml')
