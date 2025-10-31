from rest_framework.routers import DefaultRouter
from dynamicform.views import DynamicFormViewSet
from employees.views import EmployeeViewSet

router = DefaultRouter()
router.register(r'forms', DynamicFormViewSet, basename='forms')
router.register(r'employees', EmployeeViewSet, basename='employees')

urlpatterns = router.urls
