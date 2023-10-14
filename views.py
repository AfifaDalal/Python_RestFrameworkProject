from django.shortcuts import render
from .models import StudentModel
from rest_framework import viewsets,permissions
from .serializers import studentserializer

# Create your views here.

class studentviewset(viewsets.ModelViewSet):
	queryset = StudentModel.objects.all()
	serializer_class = studentserializer
	permission_classes = [permissions.IsAuthenticated]