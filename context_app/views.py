from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import (
    AgilePrinciples,
    AgileValues,
)
from .serializers import (
    AgileValueSerializer,
    AgilePrincipleSerializer,
)

# Create your views here.

class AgileValuesViewset(APIView):
    serializer_class = AgileValueSerializer
    # Retreived all data from database
    def get(self,request):
        agile_values = AgileValues.objects.all()
        serializer = AgileValueSerializer(agile_values,many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    # Create new instance in database
    def post(self,request):
        data = request.data
        serializer = AgileValueSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
    
    def perform_create(self,serializer):
        return serializer.save()



class AgilePrincipleViewset(APIView):
    serializer_class = AgilePrincipleSerializer
    # Retreived data from database
    def get(self,request):
        agile_principles = AgilePrinciples.objects.all()
        serializer = AgilePrincipleSerializer(agile_principles,many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    # create instance on the database
    def post(self,request):
        data = request.data
        serializer = AgilePrincipleSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
    
    def perform_create(self,serializer):
        return serializer.save()
        
