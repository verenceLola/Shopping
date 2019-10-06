import pytest
from shoppingList.apps.shoppingItems.models import (
    ShoppingList, Item
)
from django.urls import reverse
import freezegun


@pytest.fixture
def create_shopping_list(create_user):
    owner = create_user
    details = {
        "name": "shopping list one",
        "description": "shopping list one description",
        "owner": owner
    }
    return ShoppingList.objects.create(**details)


@pytest.fixture
def create_shopping_item(create_user):
    owner = create_user
    details = {
        "name": "shopping item one",
        "price": 300,
        "owner": owner
    }
    return Item.objects.create(**details)


@pytest.fixture
@freezegun.freeze_time('2019-10-06 11:42:59')
def create_client_shopping_list(client, generate_token):
    """
    create shopping list using api client
    """
    url = reverse('shoppingItem:list shopping lists')
    token, _ = generate_token
    details = {
        "name": "shopping list one",
        "description": "shopping list one description",
    }
    return client.post(url, details, HTTP_AUTHORIZATION='Bearer ' + token)  # noqa


@pytest.fixture
@freezegun.freeze_time('2019-10-06 12:42:59')
def add_shopping_list_items(create_client_shopping_list, client, generate_token):  # noqa
    """
    add items to a shopping list
    """
    shopping_list_id = create_client_shopping_list.data['data']['id']
    token, _ = generate_token
    url = reverse('shoppingItem:get shopping list items', args=[shopping_list_id])  # noqa
    items = [
        {
            "name": "Spirit",
            "price": 45
        },
        {
            "name": "White Meat",
            "price": 56
        }
    ]
    return client.put(
        url, items, HTTP_AUTHORIZATION='Bearer ' + token,
        content_type='application/json'
    )
