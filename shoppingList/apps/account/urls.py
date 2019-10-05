from django.urls import path
from .views import RegistrationAPIView, LoginAPIView

app_name = 'account'

urlpatterns = [
    path('users/register/', RegistrationAPIView.as_view(), name="register"),
    path('users/login/', LoginAPIView.as_view(), name="login"),
]
