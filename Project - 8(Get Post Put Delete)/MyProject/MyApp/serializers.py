from rest_framework import serializers
from .models import StudentModel


class StudentSerializer(serializers.Serializer):
    name    = serializers.CharField(max_length=100)
    age     = serializers.IntegerField()
    course  = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return StudentModel.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name   = validated_data.get('name', instance.name)
        instance.age    = validated_data.get('age', instance.age)
        instance.course = validated_data.get('course', instance.course)

        instance.save()
        return instance
    

