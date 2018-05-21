from django.shortcuts import HttpResponse
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import status
from .models import Inputs
from .serializer import InputSerializer


def home(request):
    return HttpResponse("<p>API MODE</p>")


class APITest(APIView):

    parser_classes = (MultiPartParser, )

    def get(self, request, id, format=None):
        obj = Inputs.objects.get(id=id)
        serializer = InputSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = InputSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, id, format=None):
        obj = Inputs.objects.get(id=id)
        obj.delete()
        return Response(status=status.HTTP_200_OK)