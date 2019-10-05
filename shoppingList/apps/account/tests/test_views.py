import pytest
from shoppingList.apps.account.fixtures.login import (
    correct_login, wrong_credentials, login_success_response,
    wrong_credentials_response, missing_login_email,
    missing_login_email_response,
    missing_login_password, missing_login_password_response
)
from shoppingList.apps.account.fixtures.register import (
    correct_register_data, correct_register_response,
    mismatching_passwords, mismatching_passwords_response,
    missing_confirm_password, missing_confirm_password_response,
    missing_password, missing_password_response, missing_username,
    missing_username_response, duplicate_username_and_email,
    duplicate_username_and_email_response, missing_email,
    missing_email_response
)
from django.urls import reverse
import freezegun
import datetime


@pytest.mark.parametrize(
    "credentials, expected_response ", [
        (correct_login, login_success_response),
        (wrong_credentials, wrong_credentials_response),
        (missing_login_email, missing_login_email_response),
        (missing_login_password, missing_login_password_response)
    ]
)
@pytest.mark.django_db
def test_login_POST(create_user, client, credentials, expected_response):
    """
    test login endpoint
    """
    login_url = reverse('account:login')
    response = client.post(login_url, credentials)
    if response.status_code == 200:
        assert response.data['status'] == expected_response['status']
        assert response.data['message'] == expected_response['message']
        assert response.data['data']['username'] == expected_response['data'][
            'username'
        ]
        assert response.data['data']['email'] == expected_response['data'][
            'email'
        ]
    elif response.status_code == 400:
        assert response.data == expected_response


@pytest.mark.django_db
@freezegun.freeze_time('2019-01-26 7:00:00')
def test_last_login_time(create_user, client, django_user_model):
    """
    test last login time
    """
    login_url = reverse('account:login')
    client.post(login_url, correct_login)
    last_login = django_user_model.objects.get(email=correct_login[
        'email'
    ]).last_login
    assert datetime.datetime.fromtimestamp(last_login.timestamp(
    )) == datetime.datetime(2019, 1, 26, 7)


@pytest.mark.django_db
@pytest.mark.parametrize(
    'credentials, expected_response',
    [
        (correct_register_data, correct_register_response),
        (mismatching_passwords, mismatching_passwords_response),
        (missing_confirm_password, missing_confirm_password_response),
        (missing_email, missing_email_response),
        (missing_password, missing_password_response),
        (missing_username, missing_username_response),
    ]
)
def test_register_POST(client, credentials, expected_response):
    """
    test user registration
    """
    register_url = reverse('account:register')
    response = client.post(register_url, credentials)
    assert response.data == expected_response


def test_register_duplicate_email_username(client, create_user):
    """
    test register duplicate username and email
    """
    register_url = reverse('account:register')
    response = client.post(register_url, duplicate_username_and_email)
    assert response.data == duplicate_username_and_email_response
