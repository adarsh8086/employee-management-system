from rest_framework import serializers
from .models import DynamicForm, FormField

class FormFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormField
        fields = ['id','label','name','field_type','required','order']

class DynamicFormSerializer(serializers.ModelSerializer):
    fields = FormFieldSerializer(many=True)

    class Meta:
        model = DynamicForm
        fields = ['id','name','slug','created_at','fields']

    def create(self, validated_data):
        fields_data = validated_data.pop('fields', [])
        form = DynamicForm.objects.create(**validated_data)
        for i, f in enumerate(fields_data):
            FormField.objects.create(form=form, order=i, **f)
        return form

    def update(self, instance, validated_data):
        fields_data = validated_data.pop('fields', [])
        instance.name = validated_data.get('name', instance.name)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.save()
        # Simple approach: clear and recreate fields (or implement diff)
        instance.fields.all().delete()
        for i, f in enumerate(fields_data):
            FormField.objects.create(form=instance, order=i, **f)
        return instance
