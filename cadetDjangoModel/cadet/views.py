from django.shortcuts import render
from rest_framework.views import APIView
# from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import HttpResponse

from rest_framework import status

from .models import Cadet, Roles
from .serializers import CadetSerializer, RolesSerializer


class   CadetListCreateAPIView(APIView):
    def get(self, request):
        cadets = Cadet.objects.all()
        serialized = CadetSerializer(cadets, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def post(self, request):
        serialized = CadetSerializer(data=request.data)
        if not serialized.is_valid():
            return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
        valid_data = serialized.validated_data
        serialized.create(valid_data)
        return Response(serialized.data, status=status.HTTP_201_CREATED)

class   CadetRetrieveUpdateDeleteAPIView(APIView):
    def get(self, request, pk):
        cadet = Cadet.objects.get(id=pk)
        serialized = CadetSerializer(cadet)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        cadet = Cadet.objects.get(id=pk)
        serializer = CadetSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        validated_data = serializer.validated_data
        serializer.update(cadet, validated_data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        try:
            cadet = Cadet.objects.get(id=pk)
        except:
            return Response({"error": "Cadet not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = CadetSerializer(cadet, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        Cadet.objects.filter(id=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class   RolesListCreateAPIView(APIView):
    def get(self, request):
        roles = Roles.objects.all()
        serialized = RolesSerializer(roles, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def post(self, request):
        serialized = RolesSerializer(data=request.data)
        if not serialized.is_valid():
            return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
        valid_data = serialized.validated_data
        serialized.create(valid_data)
        return Response(serialized.data, status=status.HTTP_200_OK)

class   RolesRetrieveUpdateDeleteAPIView(APIView):
    def get(self, request, pk):
        role = Roles.objects.get(id=pk)
        serialized = RolesSerializer(role)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        role = Roles.objects.get(id=pk)
        serializer = RolesSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        valid_data = serializer.validated_data
        serializer.update(role, valid_data)
        return Response(serializer.data, role)

    def patch(self, request, pk):
        try:
            role = Roles.objects.get(id=pk)
        except Roles.DoesNotExist:
            return Response({"error": "Role not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = RolesSerializer(role, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        Roles.objects.filter(id=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#EXEMPLE PATH METHOD:
#  def patch(self, request, item_id): 
#      try:
#         #Retrieve the item by Id 
#         item = Item.objects.get(id=item_id) 
#      except Item.DoesNotExist:
#             return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)
#      #Partially update with incoming data serializer Itemserializer(item, data-request.data, partial-True)
#       if serializer.is_valid():

#         #Save only the fields provided 
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_280_OK)

#      else:
#         return Response(sertalizer.errors,status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'POST'])
# def cadetView(request):
#     if request.method == 'GET':
#         cadet = Cadet.objects.all()
#         serializer = CadetSerializer(cadet, many=True)

#         return Response(serializer.data, status=status.HTTP_200_OK)
#         #return HttpResponse(serializer.data)
#     elif request.method == 'POST':
#         serializer = CadetSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         validated_data = serializer.validated_data
#         serializer.create(validated_data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['GET', 'POST'])
# def RolesView(request):
#     if request.method == 'GET':
#         roles = Roles.objects.all()
#         serializer = RolesSerializer(roles, many=True)

#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = RolesSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         validated_data = serializer.validated_data
#         serializer.create(validated_data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)