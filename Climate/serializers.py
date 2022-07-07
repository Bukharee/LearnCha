from dataclasses import fields
from rest_framework import serializers
from .models import Challange, Contribution

def create_plier():
    #TODO: a plier will be automatically created for a new challange
    pass
class CreateChallangeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Challange
        fields = ["challange_type", "title", "target"]

    def create(self, validated_data):
        request = self.context.get("request")
        user = request.user
        challange = Challange(
            **validated_data
        )
        challange.creator = user
        challange.save()
        return challange


class ViewChallangesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challange
        fields = '__all__'


class ContributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contribution
        fields = ["description", "location", "number", "picture", ]
