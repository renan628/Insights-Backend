from rest_framework import serializers

from .models import Tag
from .models import Card

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'nome')

class TagSerializerForCard(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'nome')
        extra_kwargs = {
            'nome': {'validators': []},
        }

class CardSerializer(serializers.ModelSerializer):
    tags = TagSerializerForCard(many=True, read_only=False)

    class Meta:
        model = Card
        fields = ('id', 'texto', 'tags')

    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        card = Card.objects.create(**validated_data)
        card.tags.clear()
        for tag_data in tags_data:
           tag, _ = Tag.objects.get_or_create(**tag_data)
           card.tags.add(tag)
        return card

    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags')
        instance.tags.clear()
        for tag_data in tags_data:
            tag, _ = Tag.objects.get_or_create(**tag_data)
            instance.tags.add(tag)
        return super(CardSerializer, self).update(instance, validated_data)