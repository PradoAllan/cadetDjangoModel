from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import HttpResponse

from rest_framework import status

from .models import Cadet, Roles
from .serializers import CadetSerializer, RolesSerializer

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def cadetView(request):
    if request.method == 'GET':
        cadet = Cadet.objects.all()
        serializer = CadetSerializer(cadet, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
        #return HttpResponse(serializer.data)
    elif request.method == 'POST':
        pass
        # serializer = CadetSerializer(request.data)
        # if serializer.is_valid():
        #     cadet = Cadet()
    elif request.method == 'PUT':
        pass
    elif request.method == 'PATCH':
        pass
    elif request.method == 'DELETE':
        pass


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def RolesView(request):
    if request.method == 'GET':
        roles = Roles.objects.all()
        serializer = RolesSerializer(roles, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        pass
    elif request.method == 'PUT':
        pass
    elif request.method == 'PATCH':
        pass
    elif request.method == 'DELETE':
        pass