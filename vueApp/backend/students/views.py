from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
from students.models import Student

# Create your views here.

from rest_framework.viewsets import ModelViewSet

from students.serializers import StudentSerializer

from students.models import Student

class StudentsViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

