from django.shortcuts import render
from django.http import JsonResponse
from .models import Drinks
from .serializers import DrinksSerializer
# Create your views here.

def drink_list(request):
    #get all the drinks objects
    #serialize the drinks model object
    #return the serialized JSON object
    
    drinks = Drinks.objects.all()
    #serializes all of the objects inside drink, many indicates the object is a list of objects or not
    serializer = DrinksSerializer(drinks, many=True)
    
    return JsonResponse({'Drinks':serializer.data}, safe=False)