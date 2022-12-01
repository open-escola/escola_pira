"""
COMO CRIAR UMA API REST DO ZERO COM DJANGO REST FRAMEWORK
https://www.youtube.com/watch?v=wtl8ZyCbTbg&t=865s


"""

from rest_framework import serializers

from core import models


class SomeSerializer(serializers.ModelSerializer):
    # tag_names = serializers.ReadOnlyField(read_only=True)
    # tracks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    tracks = serializers.SerializerMethodField()

    class Meta:
        model = models.Students
        fields = ('complemento', 'logradouro', 'course_id', 'tracks')


class StudentSerializers(serializers.ModelSerializer):
    # tags = serializers.SerializerMethodField()

    class Meta:
        model = models.Students
        fields = '__all__'
        # fields = ('field1', 'field2')
        depth = 1

# class Post(models.Students):
#     @property
#     def tag_names(self):
#         return self.tags.values_list('name', flat=True)
