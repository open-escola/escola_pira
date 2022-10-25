"""


"""

from rest_framework import viewsets, authentication

from core import models
from core.api import serializers


# ReadOnlyModelViewSet
class StudentsViewSet(viewsets.ModelViewSet):
    authentication_classes = [
        authentication.SessionAuthentication
    ]
    permission_classes = [
        # permissions.AllowAny
    ]

    serializer_class = serializers.StudentSerializers
    queryset = models.Students.objects.all()
