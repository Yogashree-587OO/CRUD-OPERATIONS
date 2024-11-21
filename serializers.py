
from rest_framework import serializers
from App.models import Student

class StudentSerializers(serializers.ModelSerializer):
    first_name=serializers.CharField(max_length=100)
    last_name=serializers.CharField(max_length=100)
    section=serializers.IntegerField()
    roll_no=serializers.IntegerField()

    class Meta:
        model=Student
        fields=('__all__')
        

