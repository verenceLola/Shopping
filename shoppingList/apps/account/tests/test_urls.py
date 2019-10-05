from django.urls import reverse, resolve
from shoppingList.apps.account.views import RegistrationAPIView, LoginAPIView

# test app urls resolve


def test_register_url_resolves():
    url = reverse('account:register')
    assert resolve(url).func.view_class is RegistrationAPIView


def test_login_url_resolved():
    url = reverse('account:login')
    assert resolve(url).func.view_class is LoginAPIView
