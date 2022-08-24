from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import LeadSerializer
from leads.models import Lead


@api_view(['GET'])
def index(request):
    return Response("Hello")


@api_view(['GET', 'POST'])
def lead_list(request):
    leads = Lead.objects.all()
    serializer = LeadSerializer(leads, many=True)

    if request.method == 'POST':
        serializer = LeadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def lead_detail(request,pk):
    lead = get_object_or_404(Lead, id=pk)

    if request.method == 'GET':
        serializer = LeadSerializer(lead)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = LeadSerializer(lead, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        lead.delete()
        return HttpResponse(status=204)

    return Response("Hello")

