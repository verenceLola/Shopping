correct_shopping_list_details = {
    "description": "New shopping list",
    "name": "Home Gadgets"
}
correct_shopping_list_response = {
    "status": "success",
    "message": "Shopping List Created Successfully",
    "data": {
        "id": 8,
        "description": "New shopping list",
        "items": [],
        "created_at": "2019-10-06 11:42:59",
        "updated_at": "2019-10-06 11:42:59",
        "name": "Home Gadgets",
        "budget": 0
    }
}
duplicate_shopping_list = {
    "name": "shopping list one",
    "description": "shopping list one description",
}

duplicate_shopping_list_name_response = {
    "name": [
        "Shopping List shopping list one already exists"
    ]
}

missing_shopping_list_name = {
    "description": "New shopping list"
}

missing_shopping_list_name_response = {
    "name": [
        "This field is required."
    ]
}

missing_shopping_list_description = {
    "name": "Home Gadgets"
}

missing_shopping_list_description_response = {
    "description": [
        "This field is required."
    ]
}


empty_shopping_list_response = {
    "status": "success",
    "message": "No shopping List Found",
    "data": {
        "count": 0,
        "next": None,
        "previous": None,
        "results": []
    }
}

invalid_page_response = {
    "status": "error",
    "message": "Invalid Page"
}

get_shopping_list_with_valid_id_response = {
    "status": "success",
    "message": "Shopping List details",
    "data": {
        "id": 13,
        "description": "shopping list one description",
        "items": [],
        "created_at": "2019-10-06 11:42:59",
        "updated_at": "2019-10-06 11:42:59",
        "name": "shopping list one",
        "budget": 0
    }
}

get_shopping_list_with_invalid_id_response = {
    "status": "error",
    "message": "Shopping List with id 453 not found"
}

update_shopping_list_success_response = {
    "status": "success",
    "message": "Shopping List Updated successfully",
    "data": {
        "id": 17,
        "description": "Updated jana usiku",
        "items": [],
        "created_at": "2019-10-06 11:42:59",
        "updated_at": "2019-10-06 11:42:59",
        "name": "Home Devices",
        "budget": 4600
    }
}

update_shopping_list_valid_details = {
    "budget": 4600,
    "description": "Updated jana usiku",
    "name": "Home Devices"
}

update_shopping_list_existing_name = {
    "name": "shopping list one"
}

update_shopping_list_existing_name_response = {
    "name": [
        "Shopping List shopping list one already exists"
    ]
}

update_readonly_fields_details = {
    "created_at": "2019-10-06 20:15:48.574282+03",
}

update_readonly_fields_details_response = {
    "status": "success",
    "message": "Shopping List Updated successfully",
    "data": {
        "id": 15,
        "description": "shopping list one description",
        "items": [],
        "created_at": "2019-10-06 11:42:59",
        "updated_at": "2019-10-06 11:42:59",
        "name": "shopping list one",
        "budget": 0
    }
}

add_shopping_items_success_message = {
    "status": "success",
    "message": "Item(s) added to shopping list successfully",
    "data": {
        "id": 22,
        "description": "shopping list one description",
        "items": [
            {
                "id": 9,
                "price": 45,
                "name": "Spirit",
                "bought": False
            },
            {
                "id": 10,
                "price": 56,
                "name": "White Meat",
                "bought": False
            }
        ],
        "created_at": "2019-10-06 11:42:59",
        "updated_at": "2019-10-06 11:33:48",
        "name": "shopping list one",
        "budget": 0
    }
}

get_shopping_list_items_success_response = {
    "status": "success",
    "message": "Items in the Shopping List",
    "data": [
        {
            "id": 4,
            "price": 45,
            "name": "Spirit",
            "bought": False
        },
        {
            "id": 5,
            "price": 56,
            "name": "White Meat",
            "bought": False
        }
    ]
}

get_shopping_list_items_success_missing_shopping_list_response = {
    "status": "error",
    "message": "Shopping List with id 33 not found"
}

get_shopping_list_items_of_empty_shopping_list_response = {
    "status": "success",
    "message": "No Items present in this Shopping List",
    "data": []
}

add_shopping_item = [
    {
        "price": 45,
        "name": "Spirit"
    },
    {
        "price": 56,
        "name": "White Meat"
    }
]


shopping_item_missing_name = [
    {
        "price": 56
    }
]

shopping_item_missing_name_response = {
    "name": [
        "This field may not be blank."
    ]
}

shopping_item_missing_price = [
    {
        "name": "White Meat",
    }
]

shopping_item_missing_price_response = {
    "price": [
        "A valid integer is required."
    ]
}

shopping_item_duplicate_response = {
    "items": [
        {
            "name": [
                "Shopping Item shopping item one already exists"
            ]
        }
    ]
}

duplicate_shopping_item = [
    {
        "name": "shopping item one",
        "price": 300,
    }
]

missing_shopping_list = {
    "status": "error",
    "message": "Shopping List with id 7656 not found"
}

list_shopping_items_response = {
    "count": 1,
    "next": None,
    "previous": None,
    "results": [
        {
            "id": 14,
            "name": "shopping item one",
            "price": 300,
            "bought": False
        }
    ]
}

empty_shopping_list_items_response = {
    "count": 0,
    "next": None,
    "previous": None,
    "results": []
}

list_invalid_shopping_list_item_page_response = {
    "detail": "Invalid page."
}

edit_item_correct_details = {
    "name": "Another name",
    "price": 56
}

edit_item_correct_details_response = {
    "status": "success",
    "message": "Shopping Item Updated Successfully",
    "data": {
        "id": 15,
        "price": 56,
        "name": "Another name",
        "bought": False
    }
}

edit_shopping_item_existing_name_response = {
    "name": [
        "Shopping Item shopping item one already exists"
    ]
}

edit_shopping_item_existing_name = {
    "name": "shopping item one",
}

buy_item_success_response = {
    "status": "success",
    "message": "Item marked as bought successfully",
    "data": {
        "id": 18,
        "name": "shopping item one",
        "price": 300,
        "bought": True
    }
}

buy_missing_item_response = {
    "status": "error",
    "message": "Shopping Item with id 7587 doesn't exist"
}
