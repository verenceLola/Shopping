correct_register_data = {
    "username": "someone",
    "password": "pass123",
    "email": "new@email.com",
    "confirm_password": "pass123"
}

correct_register_response = {
    "status": "success",
    "message": "Acccount created successfully",
    "data": {
        "username": "someone",
        "email": "new@email.com"
    }
}

missing_username = {
    "password": "pass123",
    "email": "new@email.com",
    "confirm_password": "pass123"
}

missing_username_response = {
    "username": [
        "Please fill in the username."
    ]
}

missing_password = {
    "username": "someone",
    "email": "new@email.com",
    "confirm_password": "pass123"
}

missing_email = {
    "username": "someone",
    "password": "pass123",
    "confirm_password": "pass123"
}

missing_email_response = {
    "email": [
        "Please fill in the email."
    ]
}

duplicate_username_and_email = {
    "username": "someone",
    "password": "pass123",
    "email": "emal@gmail.com",
    "confirm_password": "pass123"
}

duplicate_username_and_email_response = {
    "email": [
        "Email address already exists"
    ],
    "username": [
        "The username already exists. Kindly try another."
    ]
}

missing_password_response = {
    "password": [
        "Please fill in the password."
    ]
}

missing_confirm_password = {
    "username": "someone",
    "password": "pass123",
    "email": "new@email.com",
}

missing_confirm_password_response = {
    "confirm_password": [
        "Please fill in the confirm_password."
    ]
}

mismatching_passwords = {
    "username": "someone",
    "password": "pass123",
    "email": "new@email.com",
    "confirm_password": "mismatched"
}

mismatching_passwords_response = {
    "error": [
        "Those passwords don't match."
    ]
}
