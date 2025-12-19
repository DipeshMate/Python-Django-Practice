from rest_framework import serializers
from .models import StudentDetail
class StudentSerializer(serializers.Serializer):
    ids = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    roll = serializers.CharField(max_length=10)
    age = serializers.IntegerField()
    
    
    def create(self, validated_data):
        return StudentDetail.objects.create(**validated_data)