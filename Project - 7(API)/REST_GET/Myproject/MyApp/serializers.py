from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    name    = serializers.CharField(max_length = 100)
    roll    = serializers.IntegerField()
    course  = serializers.CharField(max_length = 100)

