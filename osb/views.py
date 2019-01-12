
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, JsonResponse
import json


@api_view(["POST"])
def osb(request):
    try:
        data = json.loads(request.body.decode('utf8'))
        print("hitted")
        try:
            file = {
                    'response': "hello"+data['osbResponseText']
                 }

            response = HttpResponse(JsonResponse(file), content_type='application/json')

        except IOError:
            response = HttpResponse()
        return response

    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
