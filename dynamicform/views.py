from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import DynamicForm
from .serializers import DynamicFormSerializer

class DynamicFormViewSet(viewsets.ModelViewSet):
    queryset = DynamicForm.objects.prefetch_related('fields').all().order_by('-id')
    serializer_class = DynamicFormSerializer
    permission_classes = [permissions.IsAuthenticated]
