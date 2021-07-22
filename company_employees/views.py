from django.shortcuts import render
from rest_framework import generics
from .serializers import EmployerListSerializer
from .models import Employer
from .permissions import IsOwnerOrReadOnly

# Create your views here.

class EmployerListView(generics.ListAPIView):
    serializer_class = EmployerListSerializer
    queryset = Employer.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )


class EmployerLevelListView(generics.ListAPIView):
    serializer_class = EmployerListSerializer

    def get_queryset(self):
        slug_lvl = self.kwargs['slug_level']
        return Employer.objects.filter(level__slug=slug_lvl)


