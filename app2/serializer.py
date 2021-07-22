from rest_framework import serializers
from  .models import CrudModel

class TestModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=CrudModel
        fields=['id','name','info']

class GetLimitedDataSerializer(serializers.ModelSerializer):
    class Meta:
        model=CrudModel
        fields=['name','info']
