from rest_framework import serializers
from shoppingList.apps.shoppingItems.models import ShoppingList, Item
from shoppingList.apps.account.serializers import AccountSerializer


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class ShoppingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingList
        fields = '__all__'

    owner = AccountSerializer()
    items = ItemSerializer(many=True)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
