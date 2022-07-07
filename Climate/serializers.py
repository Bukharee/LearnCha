from dataclasses import fields
from rest_framework import serializers
from .models import Challenge, Contribution


class ChallangeSerializer(serializers.ModelField):
    
    class Meta:
        model = Challenge
        fields = ["challange_type", "title", "target"]


class ContributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contribution
        fields = ["description", "location", "number", "picture", ]
