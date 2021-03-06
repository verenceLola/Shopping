from django.urls import path
from .views import (
    ListCreateShoppingList, SingleShoppingList, ShoppingListItems,
    ShoppingItemListAPIView, ShoppingItemUpdateAPIView,
    MarkShopppingItem
)

app_name = 'shoppingItem'

urlpatterns = [
    path('shoppinglist/', ListCreateShoppingList.as_view(),
         name="list shopping lists"),
    path('shoppinglist/<int:pk>/', SingleShoppingList.as_view(),
         name='view shopping list'),
    path('shoppinglist/<int:pk>/items/', ShoppingListItems.as_view(),
         name='get shopping list items'),
    path('shoppingitem/<int:pk>/', ShoppingItemUpdateAPIView.as_view(),
         name='edit-delete shoppping item'),
    path('shoppingitem/', ShoppingItemListAPIView.as_view(),
         name='list shopping items'),
    path('shoppingitem/<int:pk>/buy/', MarkShopppingItem.as_view(),
         name='buy shopping item'),
]
