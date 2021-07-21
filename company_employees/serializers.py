from rest_framework import serializers
from .models import Employer

class EmployerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = "__all__"