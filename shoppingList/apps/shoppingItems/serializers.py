from rest_framework import serializers
from shoppingList.apps.shoppingItems.models import ShoppingList, Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        exclude = ('owner',)

    price = serializers.IntegerField(required=True)

    def create(self, validated_data, **kwargs):
        """
        create a new shopping item
        """
        owner = self.context['request'].user
        validated_data['owner'] = owner
        return Item.objects.create(**validated_data)

    def validate_name(self, value):
        """
        ensure shopping list name doesn't exist
        """
        owner = self.context['request'].user
        try:
            Item.objects.get(name=value, owner=owner)
        except Item.DoesNotExist:
            return value
        raise serializers.ValidationError('Shopping Item {} already exists'.format(value))  # noqa


class ShoppingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingList
        exclude = ('owner',)

    description = serializers.CharField(required=True)
    items = ItemSerializer(many=True, required=False)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)  # noqa
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)  # noqa

    def create(self, validated_data, **kwargs):
        """
        create a new shopping list
        """
        owner = self.context['request'].user
        validated_data['owner'] = owner
        return ShoppingList.objects.create(**validated_data)

    def validate_name(self, value):
        """
        ensure shopping list name doesn't exist
        """
        owner = self.context['request'].user
        try:
            ShoppingList.objects.get(name=value, owner=owner)
        except ShoppingList.DoesNotExist:
            return value
        raise serializers.ValidationError('Shopping List {} already exists'.format(value))  # noqa

    def update(self, instance, validated_data):
        items = validated_data.pop('items', [])
        instance.description = validated_data.get('description', instance.description)  # noqa
        instance.budget = validated_data.get('budget', instance.budget)
        instance.name = validated_data.get('name', instance.name)
        for item in items:
            item_serializer = ItemSerializer(data={
                'name': item.get('name', ''),
                'price': item.get('price', '')
            }, context={'request': self.context['request']})
            item_serializer.is_valid(raise_exception=True)
            item_serializer.save()
            item_instance = item_serializer.instance
            instance.items.add(item_instance)
        instance.save()
        return instance
