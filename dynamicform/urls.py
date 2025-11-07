from django.urls import path
from .views import DynamicFormViewSet
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'forms', DynamicFormViewSet, basename='dynamicform')


urlpatterns =   [
    path('builder/', views.builder_page, name='builder_page'),  # <-- HTML page
]
urlpatterns += router.urls