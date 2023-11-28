from django.shortcuts import render
from .models import *
# Create your views here.
from rest_framework.views import APIView
from django.shortcuts import redirect
from django import forms
from rest_framework.response import Response
from .serializers import StudentSerializer
from rest_framework import status

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class StudentAPIView(APIView):
    def get(self, request, id=None):
        id = request.GET.get("id",None)
        if id:
            student = self.get_object(id)
            if not student:
                return Response("No record found", status=status.HTTP_404_NOT_FOUND)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        else:
            students = Student.objects.all()
            serializer = StudentSerializer(students, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        id = request.GET.get("id",None)
        student = self.get_object(id)
        if not student:
            return Response("No record found", status=status.HTTP_404_NOT_FOUND)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        id = request.GET.get("id",None)
        student = self.get_object(id)
        if not student:
            return Response("No record found", status=status.HTTP_404_NOT_FOUND)
        student.delete()
        return Response("Record Deleted!!", status=status.HTTP_204_NO_CONTENT)

    def get_object(self, id):
        try:
            return Student.objects.get(id=id)
        except Student.DoesNotExist:
            return None



