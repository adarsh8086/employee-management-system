from rest_framework import serializers
from .models import Employee
from dynamicform.serializers import DynamicFormSerializer
from dynamicform.models import DynamicForm

class EmployeeSerializer(serializers.ModelSerializer):
    form = DynamicFormSerializer(read_only=True)
    form_id = serializers.PrimaryKeyRelatedField(write_only=True, source='form', queryset=DynamicForm.objects.all(), required=False, allow_null=True)

    class Meta:
        model = Employee
        fields = ['id','form','form_id','data','created_by','created_at','updated_at']
        read_only_fields = ['created_by','created_at','updated_at']

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['created_by'] = user
        return super().create(validated_data)
