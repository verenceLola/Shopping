import pytest
from shoppingList.apps.account.backends import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed


def test_encode_decode_token(create_user):
    """
    test encoding and decoding JWT tokens
    """
    user = create_user
    user_data = {
        "email": user.email,
        "username": user.username
    }
    jwt = JWTAuthentication()
    # encode token
    encoded_token = jwt.generate_token(user_data)
    assert type(encoded_token) is str  # test encoding is 'utf-8'
    # decode token
    user_details = jwt.decode_token(encoded_token)
    assert user_details['userdata'] == user_data  # test token details


def test_authenticate_credentials(generate_token, django_user_model):
    """
    test authenticating JWT token against user data
    """
    access_token, user_data = generate_token
    jwt = JWTAuthentication()
    user, payload = jwt.authenticate_credentials(access_token)
    user_instance = django_user_model.objects.get(
        username=user_data['username']
    )
    assert user == user_instance
    assert payload['userdata'] == user_data


def test_expired_token(generate_expired_token, django_user_model):
    """
    test expired token
    """
    expired_access_token = generate_expired_token
    jwt = JWTAuthentication()
    with pytest.raises(AuthenticationFailed, match='Token has expired'):
        jwt.authenticate_credentials(expired_access_token)


def test_invalid_token(generate_invalid_token, django_user_model):
    """
    test invalid token
    """
    invalid_token = generate_invalid_token
    jwt = JWTAuthentication()
    with pytest.raises(AuthenticationFailed, match='Invalid token'):
        jwt.authenticate_credentials(invalid_token)
