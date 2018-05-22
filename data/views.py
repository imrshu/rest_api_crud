from django.shortcuts import HttpResponse
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import status
from .models import Inputs
from .serializer import InputSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_api_crud.settings import BASE_DIR
import os


def home(request):
    return HttpResponse("<p>API MODE</p>")


class APITest(APIView):

    parser_classes = (MultiPartParser, )

    def get(self, request, id, format=None):
        obj = Inputs.objects.get(id=id)
        serializer = InputSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @csrf_exempt
    def post(self, request, format=None):
        serializer = InputSerializer(data=request.data)
        print(request.auth)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, id, format=None):
        obj = Inputs.objects.get(id=id)
        obj.delete()
        return Response(status=status.HTTP_200_OK)

@csrf_exempt
def update_data(request,**kwargs):
    # print("BASE_DIR: ",BASE_DIR)
    if request.method == 'POST':
        if kwargs.get('slug'):
            if request.POST or request.FILES:
                myfile = ''

                print("\n[*]request.POST \n")
                for k,v in request.POST.items():
                    print('{0} : {1}'.format(k,v))
                print("\n")
                try:
                    myfile = request.FILES['file']
                except:
                    print "[*]File receive error or not received"

                if myfile:
                    print "[*]File received: ",myfile.name
                    print "[*]File size: ",myfile.size
                    handle_uploaded_file(myfile)

                return JsonResponse({'ok':'true'})
            else:
                print("[*]Empty request.POST or request.FILES")
                return JsonResponse({'ok':'false'})
        else:
            print("[*]id needed")
            return JsonResponse({'ok':'false'})
    else:
        print("Not a post request")
        return JsonResponse({'ok':'false'})

def handle_uploaded_file(f):
    filename = BASE_DIR+'/media/'+str(f.name)
    print "[*]Stored at: ",filename
    print "\n"
    with open(filename, 'wb') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
