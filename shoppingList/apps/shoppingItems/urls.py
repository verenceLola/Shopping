from django.urls import path
from .views import ListCreateShoppingList, SingleShoppingList

app_name = 'shoppingItem'

urlpatterns = [
    path('shoppinglist/', ListCreateShoppingList.as_view(),
         name="list shopping lists"),
    path('shoppinglist/<int:pk>/', SingleShoppingList.as_view(),
         name='view shopping list'),
]
