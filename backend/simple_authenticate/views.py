from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def index(request):
    return Response(data={'Hello': 'hello'})
