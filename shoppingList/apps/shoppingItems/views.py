from shoppingList.helpers.response import success_response, error_response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from shoppingList.apps.shoppingItems.models import ShoppingList
from shoppingList.apps.shoppingItems.serializers import (
    ShoppingListSerializer
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
