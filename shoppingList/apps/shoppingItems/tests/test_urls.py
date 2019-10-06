from django.urls import reverse, resolve
from shoppingList.apps.shoppingItems.views import (
    ShoppingListItems, ListCreateShoppingList,
    SingleShoppingList
)


def test_shopping_list_url_resolves():
    url = reverse('shoppingItem:list shopping lists')
    assert resolve(url).func.view_class == ListCreateShoppingList


def test_view_shopping_list_url_resolves():
    url = reverse('shoppingItem:view shopping list', args=[1])
    assert resolve(url).func.view_class == SingleShoppingList


def test_get_shopping_list_url_resolves():
    url = reverse('shoppingItem:get shopping list items', args=[1])
    assert resolve(url).func.view_class == ShoppingListItems
