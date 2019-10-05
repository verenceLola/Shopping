
correct_login = {
    "email": 'emal@gmail.com',
    "password": 'pass123'
}

login_success_response = {
    "status": "success",
    "message": "Login successful",
    "data": {
        "username": "someone",
        "email": "emal@gmail.com",
    }
}

wrong_credentials_response = {
    "error": [
        "Either your email or password isn’t right. Double check them"
    ]
}

wrong_credentials = {
    "email": "emal@gmail.com",
    "password": "wrongpass"
}

missing_login_email = {
    "password": "pass123"
}

missing_login_email_response = {
    "email": [
        "Your email address is required to log in."
    ]
}

missing_login_password = {
    "email": "emal@gmail.com"
}

missing_login_password_response = {
    "password": [
        "Kindly enter your password to log in."
    ]
}
