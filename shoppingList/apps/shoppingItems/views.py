from shoppingList.helpers.response import success_response, error_response
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateAPIView, ListAPIView,
    UpdateAPIView, DestroyAPIView
)
from shoppingList.apps.shoppingItems.models import ShoppingList, Item
from shoppingList.apps.shoppingItems.serializers import (
    ShoppingListSerializer, ItemSerializer
)
from rest_framework import status, settings, exceptions
from rest_framework.permissions import IsAuthenticated


class ListCreateShoppingList(ListCreateAPIView):
    """
    creat and list all shopping list
    """
    permission_classes = (IsAuthenticated,)
    pagination_class = settings.api_settings.DEFAULT_PAGINATION_CLASS
    serializer_class = ShoppingListSerializer

    def create(self, request, **kwargs):
        request_data = request.data
        serializer = self.serializer_class(
            data=request_data, context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = serializer.data
        return success_response(
            'Shopping List Created Successfully',
            data,
            status_code=status.HTTP_201_CREATED
        )

    def get(self, request, **kwargs):
        shopping_list = ShoppingList.objects.filter(owner=request.user)
        page = None
        try:
            page = self.paginate_queryset(shopping_list)
        except exceptions.NotFound:
            return error_response(
                'Invalid Page',
                status_code=status.HTTP_400_BAD_REQUEST
            )
        serializer = self.serializer_class(page, many=True)
        data = serializer.data
        return success_response(
            'Available Shopping Lists',
            self.get_paginated_response(data).data,
            status_code=status.HTTP_200_OK
        ) if len(data) > 0 else success_response(
            'No shopping List Found',
            self.get_paginated_response(data).data,
            status_code=status.HTTP_200_OK
        )


class SingleShoppingList(RetrieveUpdateAPIView):
    """
    view for getting a single shopping list
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = ShoppingListSerializer

    def get(self, request, pk):
        """
        return shopping list with id:<pk>
        """
        shopping_list = None
        try:
            shopping_list = ShoppingList.objects.get(pk=pk, owner=request.user)
        except ShoppingList.DoesNotExist:
            return error_response(
                'Shopping List with id {} not found'.format(pk),
                status_code=status.HTTP_404_NOT_FOUND
            )
        serializer = self.serializer_class(shopping_list)
        data = serializer.data
        return success_response(
            'Shopping List details',
            data,
            status_code=status.HTTP_200_OK
        )

    def put(self, request, pk):
        """
        update shopping list details
        """
        shopping_list = None
        try:
            shopping_list = ShoppingList.objects.get(pk=pk, owner=request.user)
        except ShoppingList.DoesNotExist:
            return error_response(
                'Shopping List with id {} not found'.format(pk),
                status_code=status.HTTP_404_NOT_FOUND
            )
        data = request.data
        serializer = self.serializer_class(shopping_list, data=data, partial=True, context={'request': request})  # noqa
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = serializer.data
        return success_response(
            'Shopping List Updated successfully',
            data,
            status_code=status.HTTP_200_OK
        )


class ShoppingListItems(RetrieveUpdateAPIView):
    """
    view for getting and adding items to a shopping list
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = ItemSerializer

    def get(self, request, pk):
        shopping_list = None
        try:
            shopping_list = ShoppingList.objects.get(pk=pk, owner=request.user)
        except ShoppingList.DoesNotExist:
            return error_response(
                'Shopping List with id {} not found'.format(pk),
                status_code=status.HTTP_404_NOT_FOUND
            )
        items = shopping_list.items
        serializer = self.serializer_class(items, many=True)
        data = serializer.data
        return success_response(
            'Items in the Shopping List',
            data,
            status_code=status.HTTP_200_OK
        ) if len(data) > 0 else success_response(
            'No Items present in this Shopping List',
            data,
            status_code=status.HTTP_200_OK
        )

    def update(self, request, pk, **kwargs):
        """
        add items to a shopping list
        """
        shopping_list = None
        try:
            shopping_list = ShoppingList.objects.get(pk=pk, owner=request.user)
        except ShoppingList.DoesNotExist:
            return error_response(
                'Shopping List with id {} not found'.format(pk),
                status_code=status.HTTP_404_NOT_FOUND
            )
        items = request.data
        serializer = ShoppingListSerializer(
            shopping_list, data={'items': items}, partial=True,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = serializer.data
        return success_response(
            'Item(s) added to shopping list successfully',
            data,
            status_code=status.HTTP_201_CREATED
        )


class ShoppingItemListAPIView(ListAPIView):
    serializer_class = ItemSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = settings.api_settings.DEFAULT_PAGINATION_CLASS

    def get(self, request):
        """
        get all shopping items for a user
        """
        items = Item.objects.filter(owner=request.user)
        page = None
        try:
            page = self.paginate_queryset(items)
        except exceptions.NotFound:
            return error_response(
                'Invalid Page',
                status_code=status.HTTP_400_BAD_REQUEST
            )
        serilizer = self.serializer_class(page, many=True)
        data = serilizer.data
        return success_response(
            'Shopping Items Available',
            self.get_paginated_response(data).data,
            status_code=status.HTTP_200_OK
        ) if len(data) > 0 else error_response(
            'No Shopping Items Available',
            status_code=status.HTTP_200_OK
        )


class ShoppingItemUpdateAPIView(UpdateAPIView, DestroyAPIView):
    serializer_class = ItemSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = settings.api_settings.DEFAULT_PAGINATION_CLASS

    def update(self, request, pk):
        """
        update an existing shopping list item
        """
        shopping_list_item = None
        updated_data = request.data
        try:
            shopping_list_item = Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            return error_response(
                "Shopping List Item with id {} doesn't exist".format(pk),  # noqa
                status_code=status.HTTP_404_NOT_FOUND
            )
        serializer = self.serializer_class(
            shopping_list_item,
            data=updated_data,
            partial=True,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = serializer.data
        return success_response(
            'Shopping Item Updated Successfully',
            data,
            status_code=status.HTTP_200_OK
        )

    def destroy(self, request, pk):
        """
        remove shopping item from shopping list
        """
        shopping_list_item = None
        try:
            shopping_list_item = Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            return error_response(
                "Shopping Item with id {} doesn't exist".format(pk),  # noqa
                status_code=status.HTTP_404_NOT_FOUND
            )
        shopping_list_item.delete()
        return success_response(
            'Shopping List Item {} removed successfully'.format(pk),
            '',
            status_code=status.HTTP_200_OK
        )
