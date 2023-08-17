#converts a python model object to JSON.
from rest_framework import serializers
from .models import Drinks

#serializer class for Drinks model
class DrinksSerializer(serializers.ModelSerializer):
    #describes the models meta data
    class Meta:
        #model object for transforming into JSON object
        model = Drinks
        #used as key name for transforming the model to JSON object
        fields =  ['id', 'name', 'description']