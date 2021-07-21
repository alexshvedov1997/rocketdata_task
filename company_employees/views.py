from django.shortcuts import render
from rest_framework import generics
from .serializers import EmployerListSerializer
from .models import Employer

# Create your views here.

class EmployerListView(generics.ListAPIView):
    serializer_class = EmployerListSerializer
    queryset = Employer.objects.all()

