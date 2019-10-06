from rest_framework import serializers
from shoppingList.apps.shoppingItems.models import ShoppingList, Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class ShoppingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingList
        exclude = ('owner',)

    # owner = AccountSerializer(required=False)
    description = serializers.CharField(required=True)
    items = ItemSerializer(many=True, required=False)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)  # noqa
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)  # noqa

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
