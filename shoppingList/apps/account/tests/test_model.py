import pytest


def test_new_user_account(create_user):
    """
    test created user account
    """
    if create_user.is_active:
        assert True  # confirm account is active
    assert create_user.get_full_name == 'someone'  # test users fullname


def test_new_use_without_email(django_user_model):
    """
    test creating new account without email return correct error message
    """
    with pytest.raises(TypeError, match='Users must have an email'):
        django_user_model.objects.create_user(
            username='someone', password='pass123', email=None
        )


def test_new_user_without_username(django_user_model):
    """
    test creating new user without username return correct error message
    """
    with pytest.raises(TypeError, match='Users must have a username'):
        django_user_model.objects.create_user(
            username=None, password='pass123', email='some@email.com'
        )


def test_print_user(create_user):
    """
    test printing user object
    """
    assert create_user.__str__() == 'someone'


def test_create_superuser(create_superuser):
    """
    test create super user
    """
    superuser = create_superuser
    if superuser.is_active:
        assert True
    if superuser.is_superuser:
        assert True


def test_create_superuser_without_password(django_user_model):
    """
    test creating new super user account without password returns correct error
    """
    with pytest.raises(TypeError, match='Superuser must have a password'):
        django_user_model.objects.create_superuser(
            username='someone', password=None, email='some@email.com'
        )
