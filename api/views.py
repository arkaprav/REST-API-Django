from django.shortcuts import render
from django.http import JsonResponse
from .models import Drinks
from .serializers import DrinksSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


#readonly endpoint
#it takes a get request from the server and returns the serialized JSON data
@api_view(['GET','POST'])#defines which request methods are valid on the api call
def drink_list(request, format=None):
    if request.method == 'GET':
        #get all the drinks objects
        #serialize the drinks model object
        #return the serialized JSON object
        
        drinks = Drinks.objects.all()
        #serializes all of the objects inside drink, many indicates the object is a list of objects or not
        serializer = DrinksSerializer(drinks, many=True)
        
        return Response(serializer.data)
    
    if request.method == 'POST':
        #post request toput data on table
        #the data coming fromtheresponse is being deserilizedusing deserializer
        deserializer = DrinksSerializer(data=request.data)
        #check the Deserialized JSON object is invalid format for entering data into table
        if deserializer.is_valid():
            deserializer.save()
            #if valid update data to table
            #give back a response with data and status code successfully created
            #Response is a response of restframework not of the json response
            return Response(deserializer.data, status=status.HTTP_201_CREATED)
        #if data is not valis deserailizer returns an error
        return Response(deserializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def drink_details(request, id,format=None):
    try:
        drink = Drinks.objects.get(pk=id)
    except Drinks.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = DrinksSerializer(drink)
        return Response(serializer.data)
    elif request.method == 'PUT':
        deserializer = DrinksSerializer(drink, data=request.data)
        if deserializer.is_valid():
            deserializer.save()
            return Response(deserializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(deserializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)