from rest_framework import serializers

from .models import (
    AgileValues,
    AgilePrinciples,
)


class AgilePrincipleSerializer(serializers.ModelSerializer):
    """
    Validating and Serializing AgilePrinciples objects
    """
    heading = serializers.CharField(max_length=255)
    definition = serializers.CharField()

    class Meta:
        model = AgilePrinciples
        fields = '__all__'

    def create(self, validated_data):
        return AgilePrinciples.objects.create(**validated_data)

    def update(self, instance, validated_data): 
        instance.heading = validated_data.get('heading', instance.heading)
        instance.definition = validated_data.get('definition', instance.definition)

        return instance



class AgileValueSerializer(serializers.ModelSerializer):
    """
    Validating and Serializing AgileAgileValueSerializer objects
    """
    heading = serializers.CharField(max_length=255)
    definition = serializers.CharField()

    class Meta:
        model = AgileValues
        fields = '__all__'

    def create(self, validated_data):
        return AgileValues.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.heading = validated_data.get('heading', instance.heading)
        instance.definition = validated_data.get('definition', instance.definition)

        return instance