import freezegun
import datetime
from django.utils import timezone


def test_create_new_shopping_list(create_shopping_list):
    """
    test new list created with no item, and budget of 0
    """
    shopping_list = create_shopping_list
    assert shopping_list.items.values_list().count() == 0
    assert shopping_list.budget == 0

def test_create_new_shopping_list_correct_user(create_user, create_shopping_list):  # noqa
    """
    test new list has the correct user
    """
    shopping_list = create_shopping_list
    owner = create_user
    assert shopping_list.owner == owner


@freezegun.freeze_time('2019-10-06 13:45:27.415444+03')
def test_new_shopping_list_created_with_correct_time(create_shopping_list):
    """
    test new shopping list has correct created_at field
    """
    shopping_list = create_shopping_list
    created_at = datetime.datetime.fromtimestamp(shopping_list.created_at.timestamp()) # noqa
    assert shopping_list.created_at.day == timezone.now().day


def test_printing_shopping_list_print_name(create_shopping_list):
    """
    test printing shoppinglist prints its name
    """
    shopping_list = create_shopping_list
    assert shopping_list.__str__() == 'shopping list one'


def test_creating_shopping_item(create_shopping_item, create_user):
    """
    test creating new shopping item assigns correct owner
    """
    owner = create_user
    shopping_item = create_shopping_item
    assert shopping_item.owner == owner


def test_adding_item_to_list(create_shopping_item, create_shopping_list):
    """
    test adding shopping item to shopping list
    """
    shopping_list = create_shopping_list
    items_before = shopping_list.items.values_list().count()
    new_item = create_shopping_item
    shopping_list.items.add(new_item)
    items_after = shopping_list.items.values_list().count()
    assert items_after > items_before
    assert items_before == 0
    assert items_after == 1


def test_printing_shoppping_item_returns_name(create_shopping_item):
    """
    test printing shopping item prints its name
    """
    item = create_shopping_item
    assert item.__str__() == 'shopping item one'
