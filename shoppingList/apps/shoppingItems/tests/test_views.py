import pytest
from django.urls import reverse
from shoppingList.conftest import get_shopping_list
import freezegun
from .fixtures import (
    correct_shopping_list_details, correct_shopping_list_response,
    duplicate_shopping_list_name_response, missing_shopping_list_description,
    missing_shopping_list_description_response, duplicate_shopping_list,
    missing_shopping_list_name, missing_shopping_list_name_response,
    empty_shopping_list_response, invalid_page_response, add_shopping_item,
    get_shopping_list_with_valid_id_response, shopping_item_duplicate_response,
    get_shopping_list_with_invalid_id_response, update_readonly_fields_details,
    update_readonly_fields_details_response, shopping_item_missing_name,
    update_shopping_list_existing_name, add_shopping_items_success_message,
    get_shopping_list_items_success_response, shopping_item_missing_price,
    get_shopping_list_items_success_missing_shopping_list_response,
    update_shopping_list_existing_name_response, duplicate_shopping_item,
    update_shopping_list_success_response, update_shopping_list_valid_details,
    get_shopping_list_items_of_empty_shopping_list_response,
    shopping_item_missing_price_response, shopping_item_missing_name_response,
    missing_shopping_list, list_shopping_items_response,
    empty_shopping_list_items_response, edit_item_correct_details,
    list_invalid_shopping_list_item_page_response,
    edit_shopping_item_existing_name_response,
    edit_shopping_item_existing_name, edit_item_correct_details_response,
    buy_item_success_response, buy_missing_item_response
)
from shoppingList.apps.shoppingItems.models import Item


def test_create_new_shopping_list_has_correct_owner(client, generate_token,django_user_model):  # noqa
    """
    test new shopping list has correct owner
    """
    url = reverse('shoppingItem:list shopping lists')
    token, user_details = generate_token
    details = {
        "name": "shopping list 1",
        "description": "shopping list 1 desription",
    }
    client.post(url, details, HTTP_AUTHORIZATION='Bearer ' + token)
    shopping_list = get_shopping_list(**details)
    assert shopping_list.owner == django_user_model.objects.get(**user_details)


@freezegun.freeze_time('2019-10-06 11:42:59')
@pytest.mark.parametrize(
    "shopping_list_details, expected_response",
    [
        (correct_shopping_list_details, correct_shopping_list_response),
        (duplicate_shopping_list, duplicate_shopping_list_name_response),
        (missing_shopping_list_name, missing_shopping_list_name_response),
        (missing_shopping_list_description, missing_shopping_list_description_response)  # noqa
    ]
)
def test_created_new_list(client, generate_token,create_shopping_list, shopping_list_details, expected_response):  # noqa
    """
    test response when shopping list created successfully
    """
    url = reverse('shoppingItem:list shopping lists')
    token, _ = generate_token
    response = client.post(
        url, shopping_list_details, HTTP_AUTHORIZATION='Bearer ' + token
    )
    assert response.data == expected_response


def test_get_shopping_list_when_empty(client, generate_token):
    """
    test getting paginated shopping list
    """
    url = reverse('shoppingItem:list shopping lists')
    token, _ = generate_token
    response = client.get(url, HTTP_AUTHORIZATION='Bearer ' + token)
    assert response.data == empty_shopping_list_response


def test_get_shopping_list_invalid_page(client, generate_token):
    """
    test getting invalid shopping list page
    """
    url = reverse('shoppingItem:list shopping lists')
    token, _ = generate_token
    response = client.get(url + '?page=345', HTTP_AUTHORIZATION='Bearer ' + token)  # noqa
    assert response.data == invalid_page_response


def test_get_shopping_list_if_not_owner(client, generate_token, generate_token2):  # noqa
    """
    test getting shopping list if not owner
    """
    url = reverse('shoppingItem:list shopping lists')
    token1, _ = generate_token
    token2, _ = generate_token2
    # create shopping for user1
    client.post(url, correct_shopping_list_details, HTTP_AUTHORIZATION='Bearer ' + token1)  # noqa
    # try getting shopping list for user2
    response = client.get(url, HTTP_AUTHORIZATION='Bearer ' + token2)  # noqa
    assert response.data == empty_shopping_list_response


@pytest.mark.parametrize(
    "shopping_list_id, expected_response",
    [
        (13, get_shopping_list_with_valid_id_response),
        (453, get_shopping_list_with_invalid_id_response)
    ]
)
def test_get_single_shopping_list(client, create_client_shopping_list, generate_token, shopping_list_id, expected_response):  # noqa
    """
    test getting single shopping list
    """
    url = reverse('shoppingItem:view shopping list', args=[shopping_list_id])
    token, _ = generate_token
    response = client.get(url,  HTTP_AUTHORIZATION='Bearer ' + token)  # noqa
    assert response.data == expected_response


@freezegun.freeze_time('2019-10-06 11:42:59')
@pytest.mark.parametrize(
    "shopping_list_id, new_details, expected_response",
    [
        (15, update_readonly_fields_details, update_readonly_fields_details_response),  # noqa
        (16, update_shopping_list_existing_name, update_shopping_list_existing_name_response),  # noqa
        (17, update_shopping_list_valid_details, update_shopping_list_success_response),  # noqa
        (453, update_shopping_list_success_response, get_shopping_list_with_invalid_id_response),  # noqa
    ]
)
def test_update_shopping_list(client, create_client_shopping_list, generate_token, shopping_list_id, new_details, expected_response):  # noqa
    """
    test edit shopping list details
    """
    url = reverse('shoppingItem:view shopping list', args=[shopping_list_id])
    token, _ = generate_token
    response = client.put(
        url, new_details, HTTP_AUTHORIZATION='Bearer ' + token,
        content_type='application/json'
    )
    assert response.data == expected_response


@pytest.mark.parametrize(
    "shopping_list_id, expected_response",
    [
        (19, get_shopping_list_items_success_response),
        (33, get_shopping_list_items_success_missing_shopping_list_response)
    ]
)
def test_get_shopping_list_items(client, generate_token, add_shopping_list_items, shopping_list_id, expected_response):  # noqa
    """
    test get shopping list items
    """
    url = reverse('shoppingItem:get shopping list items', args=[shopping_list_id])  # noqa
    token, _ = generate_token
    response = client.get(url, HTTP_AUTHORIZATION='Bearer ' + token)
    assert response.data == expected_response


def test_get_shopping_list_items_of_empty_shopping_list(client, generate_token, create_shopping_list):  # noqa
    """
    test geting items of an empty shopping list
    """
    shopping_list = create_shopping_list
    url = reverse('shoppingItem:get shopping list items', args=[shopping_list.id])  # noqa
    token, _ = generate_token
    response = client.get(url, HTTP_AUTHORIZATION='Bearer ' + token)
    assert response.data == get_shopping_list_items_of_empty_shopping_list_response  # noqa


@freezegun.freeze_time('2019-10-06 11:33:48')
@pytest.mark.parametrize(
    "item_details, expected_response",
    [
        (add_shopping_item, add_shopping_items_success_message),
        (shopping_item_missing_name, shopping_item_missing_name_response),  # noqa
        (duplicate_shopping_item, shopping_item_duplicate_response),
        (shopping_item_missing_price, shopping_item_missing_price_response),
    ]
)
def test_add_shopping_item_to_shopping_list(client, generate_token, create_client_shopping_list, create_shopping_item, item_details, expected_response):  # noqa
    """
    test adding duplicate items to shopping list
    """
    shopping_list = create_client_shopping_list.data
    token, _ = generate_token
    url = reverse('shoppingItem:get shopping list items', args=[shopping_list['data']['id']])  # noqa
    response = client.put(
        url, item_details, HTTP_AUTHORIZATION='Bearer ' + token,
        content_type='application/json'
    )
    assert response.data == expected_response

def test_add_shopping_item_to_missing_shopping_list(client, generate_token):  # noqa
    """
    test add shopping item to missing list
    """
    token, _ = generate_token
    missing_shopping_list_id = 7656
    url = reverse('shoppingItem:get shopping list items', args=[missing_shopping_list_id])  # noqa
    response = client.put(
        url, {}, HTTP_AUTHORIZATION='Bearer ' + token,
        content_type='application/json'
    )
    assert response.data == missing_shopping_list


def test_list_shopping_items(client, generate_token, create_shopping_item):
    """
    test list shopping items
    """
    url = reverse('shoppingItem:list shopping items')
    token, _ = generate_token
    response = client.get(url, HTTP_AUTHORIZATION='Bearer ' + token)
    assert response.data == list_shopping_items_response


def test_list_empty_shopping_items(client, generate_token):
    """
    test listing non available items
    """
    url = reverse('shoppingItem:list shopping items')
    token, _ = generate_token
    response = client.get(url, HTTP_AUTHORIZATION='Bearer ' + token)
    assert response.data == empty_shopping_list_items_response


def test_list_invalid_shopping_list_item_page(client, generate_token):
    """
    test list invalid page for item
    """
    url = reverse('shoppingItem:list shopping items')
    token, _ = generate_token
    response = client.get(url + '?page=343', HTTP_AUTHORIZATION='Bearer ' + token)  # noqa
    assert response.data == list_invalid_shopping_list_item_page_response


@pytest.mark.parametrize(
    "new_data, expected_response",
    [
        (edit_item_correct_details, edit_item_correct_details_response),  # noqa
        (edit_shopping_item_existing_name, edit_shopping_item_existing_name_response)  # noqa
    ]
)
def test_update_shopping_item(client, create_shopping_item, generate_token, new_data, expected_response):  # noqa
    """
    test update shopping item
    """
    item = create_shopping_item
    url = reverse('shoppingItem:edit-delete shoppping item', args=[item.id])
    token, _ = generate_token
    response = client.put(
        url, new_data, HTTP_AUTHORIZATION='Bearer ' + token,
        content_type='application/json',
    )
    assert response.data == expected_response


def test_edit_missing_shopping_item(client, generate_token):
    """
    test edit missing shopping item
    """
    missing_item = 5757
    expected_response = {
        "status": "error",
        "message": "Shopping Item with id {} doesn't exist".format(missing_item)  # noqa
    }
    token, _ = generate_token
    url = reverse('shoppingItem:edit-delete shoppping item', args=[missing_item])  # noqa
    response = client.put(
        url, {}, HTTP_AUTHORIZATION='Bearer ' + token,
        content_type='application/json',
    )
    assert response.data == expected_response


def test_delete_missing_shopping_item(client, generate_token):
    """
    test delete missing shopping item
    """
    missing_item = 5757
    expected_response = {
        "status": "error",
        "message": "Shopping Item with id {} doesn't exist".format(missing_item)  # noqa
    }
    token, _ = generate_token
    url = reverse('shoppingItem:edit-delete shoppping item', args=[missing_item])  # noqa
    response = client.delete(
        url, {}, HTTP_AUTHORIZATION='Bearer ' + token,
        content_type='application/json',
    )
    assert response.data == expected_response


def test_delete_shopping_item(client, generate_token, create_shopping_item):  # noqa
    """
    test delete shopping item
    """
    id = create_shopping_item.id
    url = reverse('shoppingItem:edit-delete shoppping item', args=[id])
    token, _ = generate_token
    expected_response = {
        "status": "success",
        "message": "Shopping List Item {} removed successfully".format(id),
        "data": ""
    }
    response = client.delete(
        url, {}, HTTP_AUTHORIZATION='Bearer ' + token,
        content_type='application/json',
    )
    assert response.data == expected_response
    with pytest.raises(create_shopping_item.DoesNotExist):
        Item.objects.get(pk=id)


def test_mark_item_as_bought(client, create_shopping_item, generate_token):
    """
    test user can mark item as bought
    """
    item = create_shopping_item
    url = reverse('shoppingItem:buy shopping item', args=[item.id])
    token, _ = generate_token
    response = client.get(url, HTTP_AUTHORIZATION='Bearer ' + token)
    assert Item.objects.get(pk=item.id).bought
    assert response.status_code == 200
    assert response.data == buy_item_success_response


def test_mark_missing_item_as_bought(client, generate_token):
    """
    test marking missing item as bought
    """
    missing_id = 7587
    url = reverse('shoppingItem:buy shopping item', args=[missing_id])
    token, _ = generate_token
    response = client.get(url, HTTP_AUTHORIZATION='Bearer ' + token)
    assert response.status_code == 404
    assert response.data == buy_missing_item_response
    with pytest.raises(Item.DoesNotExist):
        Item.objects.get(pk=missing_id)
