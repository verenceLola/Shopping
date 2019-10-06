from django.urls import path
from .views import ListCreateShoppingList

app_name = 'shoppingItem'

urlpatterns = [
    path('shoppinglist/', ListCreateShoppingList.as_view(),
         name="list shopping"),
]
