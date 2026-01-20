import requests

import requests


def test_get_users():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)

    # status code tekshirish
    assert response.status_code == 200

    # ma'lumot turi tekshirish
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

    print("CI Test project Docker ichida ishlayapti 🚀")

