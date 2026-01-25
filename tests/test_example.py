import requests

def test_get_users():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    print("Test 1: Users endpoint Docker ichida ishlayapti 🚀")

def test_get_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    print("Test 2: Posts endpoint Docker ichida ishlayapti 🚀")

def test_get_todos():
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    print("Test 3: Todos endpoint Docker ichida ishlayapti 🚀")

def test_get_albums():
    url = "https://jsonplaceholder.typicode.com/albums"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    print("Test 4: Albums endpoint Docker ichida ishlayapti 🚀")

def test_get_photos():
    url = "https://jsonplaceholder.typicode.com/photos"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    print("Test 5: Photos endpoint Docker ichida ishlayapti 🚀")

def test_get_user_1():
    url = "https://jsonplaceholder.typicode.com/users/1"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert data["id"] == 1
    print("Test 6: User 1 endpoint Docker ichida ishlayapti 🚀")

def test_get_post_1():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert data["id"] == 1
    print("Test 7: Post 1 endpoint Docker ichida ishlayapti 🚀")

def test_get_todo_1():
    url = "https://jsonplaceholder.typicode.com/todos/1"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert data["id"] == 1
    print("Test 8: Todo 1 endpoint Docker ichida ishlayapti 🚀")

def test_get_album_1():
    url = "https://jsonplaceholder.typicode.com/albums/1"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert data["id"] == 1
    print("Test 9: Album 1 endpoint Docker ichida ishlayapti 🚀")

def test_get_photo_1():
    url = "https://jsonplaceholder.typicode.com/photos/1"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert data["id"] == 1
    print("Test 10: Photo 1 endpoint Docker ichida ishlayapti 🚀")
    print("Test 10: Photo 1 endpoint Docker ichida ishlayapti 🚀")


