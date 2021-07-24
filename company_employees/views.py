from django.shortcuts import render
from rest_framework import generics
from .serializers import EmployerListSerializer
from .models import Employer
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

# Create your views here.

class EmployerListView(generics.ListAPIView):
    serializer_class = EmployerListSerializer
    queryset = Employer.objects.all()
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticated )


class EmployerLevelListView(generics.ListAPIView):
    serializer_class = EmployerListSerializer
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticated )
    def get_queryset(self):
        slug_lvl = self.kwargs['slug_level']
        return Employer.objects.filter(level__slug=slug_lvl)


class EmployerDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmployerListSerializer
    queryset = Employer.objects.all()
    authentication_classes = (TokenAuthentication,)
