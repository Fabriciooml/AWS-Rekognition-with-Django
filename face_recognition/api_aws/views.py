from django.shortcuts import render
from .models import Face
from rest_framework import viewsets
from .serializers import FaceSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Face
#from .apps import face_recognition, take_frames

def face_api(request):

    if request.method=='POST':
        Face.recognize()
        
        # Faça aqui o que vc for precisos com os dados recebidos

    return render(request, 'face_api.html')