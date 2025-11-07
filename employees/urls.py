from rest_framework.routers import DefaultRouter
from dynamicform.views import DynamicFormViewSet
from employees.views import EmployeeViewSet

router = DefaultRouter()
router.register(r'forms', DynamicFormViewSet, basename='forms')
router.register(r'employees', EmployeeViewSet, basename='employees')



from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='employee_list'),
    path('create/', views.create_view, name='employee_create'),
   
]
urlpatterns += router.urls 