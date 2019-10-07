from django.urls import reverse


def test_list_all_notifications(client, generate_token, notication_creation):  # noqa
    """
    test retrieve notifications
    """
    url = reverse('notifications:notifications')
    notification = notication_creation
    token, _ = generate_token
    response = client.get(url, HTTP_AUTHORIZATION='Bearer ' + token)
    assert response.status_code == 200
    assert notification.__str__() == "You've got  a message"
    notification.read = True
    response = client.get(url, HTTP_AUTHORIZATION='Bearer ' + token)
    assert response.status_code == 200
