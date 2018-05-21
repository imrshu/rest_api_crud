from rest_framework.serializers import ModelSerializer
from .models import Category, Inputs


class InputSerializer(ModelSerializer):
    class Meta:
        model = Inputs
        fields = '__all__'
