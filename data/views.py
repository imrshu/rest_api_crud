from django.shortcuts import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Inputs
from .serializer import InputSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_api_crud.settings import BASE_DIR
import base64, ast

def home(request):
    return HttpResponse("<p>API MODE</p>")

class APITest(APIView):

    def get(self, request, id, format=None):
        obj = Inputs.objects.get(id=id)
        serializer = InputSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)


@csrf_exempt
def update_data2(request,**kwargs):
    if request.method == 'POST':
        try:
            if request.body:
                # Decode the request body to utf-8 format
                body = ast.literal_eval(request.body.decode('utf-8'))
                # Send file base64 encoded form along with actual file name
                handle_uploaded_file(body['file']['value'], body['file']['filename'])
                return JsonResponse({'ok':'true'})
            else:
                return JsonResponse({'ok':'false'})
        except:
            return JsonResponse({'ok':'false'})
    else:
        return JsonResponse({'Method':'Not Allowed'})


def handle_uploaded_file(file_encoded_val, file_name):
    # Make a temp file with actual file name
    filename = BASE_DIR+'/media/'+str(file_name)
    # Decode the base64 encoded form 
    original_file_chunks = base64.b64decode(file_encoded_val)
    with open(filename, 'wb') as original_file:
        # Write the decoded form to temp file
        original_file.write(original_file_chunks)
