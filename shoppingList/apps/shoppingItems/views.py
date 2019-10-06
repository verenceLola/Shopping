from shoppingList.helpers.response import success_response, error_response
from rest_framework.generics import ListCreateAPIView
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
