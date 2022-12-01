"""



"""

import json

import pandas as pd
from django.http import JsonResponse
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import CustomUser, Students


# @login_required
def go_api_model(request):
    # Using Model
    return JsonResponse(
        list(CustomUser.objects.all().values()),
        safe=False,
        content_type='application/json'
    )


#@login_required
def go_api_model_student(request):
    # Using Model
    return JsonResponse(
        list(Students.objects.all().values()),
        safe=False,
        content_type='application/json'
    )


#@login_required
def go_api_dataframe(request):
    # Using Pandas
    details = {
        'Name': ['Ankit', 'Aishwarya', 'Shaurya', 'Shivangi'],
        'Age': [23, 21, 22, 21],
        'University': ['BHU', 'JNU', 'DU', 'BHU'],
    }
    df = pd.DataFrame(details)
    result = df.to_json(orient='records')
    parsed = json.loads(result)
    return JsonResponse(parsed, safe=False)


class APIRest(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    O que eu escrever aqui aparece!
    """
    authentication_classes = [
        # authentication.TokenAuthentication,
        # authentication.BasicAuthentication,
        authentication.SessionAuthentication
    ]
    permission_classes = [
        # permissions.IsAdminUser,
        permissions.AllowAny
    ]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = {user.cep for user in Students.objects.all()}
        return Response(usernames)
