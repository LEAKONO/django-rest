from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
from.serializers import PersonSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET'])
def get_all_people(request):
    people=Person.objects.all()
    serializer=PersonSerializer(people,many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_person(request):
    serializer=PersonSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)



