from django.urls import path
from .views import DynamicFormViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'forms', DynamicFormViewSet, basename='dynamicform')

urlpatterns = router.urls
