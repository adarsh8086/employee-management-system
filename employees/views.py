from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from django.db.models import Q
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.select_related('created_by','form').all().order_by('-created_at')
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.query_params.get('q')
        form_id = self.request.query_params.get('form')
        if form_id:
            qs = qs.filter(form_id=form_id)
        if q:
            
            qs = qs.filter(data__icontains=q)
        return qs
   

def home_view(request):
    return render(request, 'employees/list.html')


