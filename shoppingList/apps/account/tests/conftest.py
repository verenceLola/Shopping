
import pytest
from shoppingList.apps.account.backends import JWTAuthentication
from freezegun import freeze_time


@pytest.fixture
def create_superuser(django_user_model):
    """
    create new superuser account
    """
    superuser = django_user_model.objects.create_superuser(
        username='someone', password='pass123', email='emal@gmail.com'
    )
    return superuser


@pytest.fixture
def generate_invalid_token():
    """
    generate invalid JWT
    """
    jwt = JWTAuthentication()
    user_data = {
        "email": "invalid@email.org",
        "username": "invalid"
    }
    # encode data with invalid data
    encoded_token = jwt.generate_token(user_data)
    return encoded_token


@pytest.fixture
@freeze_time('2019-05-26 8:00:00')
def generate_expired_token(create_user):
    """
    generate expired JWT token
    """
    user = create_user
    user_data = {
        "email": user.email,
        "username": user.username
    }
    jwt = JWTAuthentication()
    # encode token
    encoded_token = jwt.generate_token(user_data)
    return encoded_token
