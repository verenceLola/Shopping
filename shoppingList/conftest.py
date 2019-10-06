import pytest
from shoppingList.apps.account.backends import JWTAuthentication
from shoppingList.apps.shoppingItems.models import ShoppingList


@pytest.fixture
def create_user(django_user_model):
    """
    create new user account
    """
    user = django_user_model.objects.create_user(
        username='someone', email='emal@gmail.com', password='pass123'
    )
    return user


@pytest.fixture
def generate_token(create_user):
    """
    generate JWT token
    """
    user = create_user
    user_data = {
        "email": user.email,
        "username": user.username
    }
    jwt = JWTAuthentication()
    # encode token
    encoded_token = jwt.generate_token(user_data)
    return encoded_token, user_data


@pytest.fixture
def set_owner(django_user_model, user_details):
    """
    fixture for adding item owner
    """
    return django_user_model.objects.create_user(**user_details)


@pytest.fixture
def add_shopping_list(set_owner, owner, details):
    """
    fixture for adding a shopping list
    """
    owner = set_owner(owner)
    details['owner'] = owner
    return ShoppingList.objects.create(**details)


@pytest.mark.django_db
def get_shopping_list(**details):
    """
    retrive shopping list by pk
    """
    return ShoppingList.objects.get(**details)


@pytest.fixture
def create_user2(django_user_model):
    """
    create another user
    """
    user = django_user_model.objects.create_user(
        username='user_2', email='another@gmail.com', password='pass123'
    )
    return user


@pytest.fixture
def generate_token2(create_user2):
    """
    generate token for user2
    """
    user = create_user2
    user_data = {
        "email": user.email,
        "username": user.username
    }
    jwt = JWTAuthentication()
    # encode token
    encoded_token = jwt.generate_token(user_data)
    return encoded_token, user_data
