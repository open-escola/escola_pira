"""
COMO CRIAR UMA API REST DO ZERO COM DJANGO REST FRAMEWORK
https://www.youtube.com/watch?v=wtl8ZyCbTbg&t=865s


"""

from rest_framework import serializers

from core import models


class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Students
        fields = '__all__'
        # fields = ('field1', 'field2')
