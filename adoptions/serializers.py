from rest_framework import serializers
from .models import Pet


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ('name','submitter','species','sex','age')

    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     data['young'] = instance.age < 3 and 'Yes' or 'No'
    #     return data