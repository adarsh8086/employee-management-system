from django.db import models
from django.db import models
# from django.contrib.postgres.fields import JSONField 

class DynamicForm(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class FormField(models.Model):
    FIELD_TYPES = [
        ('text', 'Text'),
        ('number', 'Number'),
        ('date', 'Date'),
        ('password', 'Password'),
        ('email', 'Email'),
        ('textarea', 'Textarea'),
        # add more types if needed
    ]

    form = models.ForeignKey(DynamicForm, related_name='fields', on_delete=models.CASCADE)
    label = models.CharField(max_length=150)
    name = models.CharField(max_length=150)  # machine-friendly name, e.g., "phone"
    field_type = models.CharField(max_length=30, choices=FIELD_TYPES)
    required = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)  # for ordering

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.form.name} - {self.label}"

