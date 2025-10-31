from django.db import models
from django.db import models
from django.conf import settings
# If using Django 3.1+:
from django.db.models import JSONField

from dynamicform.models import DynamicForm

class Employee(models.Model):
    form = models.ForeignKey(DynamicForm, related_name='employees', on_delete=models.SET_NULL, null=True, blank=True)
    # store dynamic responses as JSON e.g. {"name":"John","phone":"1234", "dob":"1990-01-01"}
    data = JSONField()  # Django's JSONField
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # try to display a friendly name if exists in JSON
        try:
            name = self.data.get('name') or self.data.get('Name')
            return name or f"Employee {self.id}"
        except Exception:
            return f"Employee {self.id}"

