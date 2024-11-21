from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from App.models import Student
from App.serializers import StudentSerializers





class Student1(APIView):
    def post(self, request):
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'students': serializer.data}, status=200)
        else:
            return Response({'status': 'error', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



# get 
class Getview (APIView):
    def get(self,args,*kwargs):
        result=Student.objects.all()
        serializer = StudentSerializers(result,many=True)
        return Response({'ststus':'success','students':serializer.data},status=200)
# Delete
class Deleteview (APIView):
    def delete(self,request,id):
        result=Student.objects.get(id=id)
        Student.delete()
        serializer = StudentSerializers(result,many=True)
        return Response({'ststus':'success','students':serializer.data},status=200)
    #put



class PutView(APIView):
    def put(self, request, id, *args, **kwargs):
        try:
            student = Student.objects.get(id=id)
        except Student.DoesNotExist:
            return Response({'status': 'fail', 'message': 'Student not found'}, status=404)

        # Deserialize and validate the data for updating the entire student record
        serializer = StudentSerializers(student, data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the updated data
            return Response({'status': 'success', 'students': serializer.data}, status=200)
        return Response({'status': 'fail', 'errors': serializer.errors}, status=400)
    #patch


class PatchView(APIView):
    def patch(self, request, id, *args, **kwargs):
        try:
            student = Student.objects.get(id=id)
        except Student.DoesNotExist:
            return Response({'status': 'fail', 'message': 'Student not found'}, status=404)

        # Deserialize and validate only the partial data provided in the request
        serializer = StudentSerializers(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()  # Save the partially updated data
            return Response({'status': 'success', 'students': serializer.data}, status=200)
        return Response({'status': 'fail', 'errors': serializer.errors}, status=400)
    
    



