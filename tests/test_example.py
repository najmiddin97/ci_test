import requests
import allure


@allure.feature("Users API")
@allure.story("Get users list")
@allure.title("GET /users returns user list")
def test_get_users():
    url = "https://jsonplaceholder.typicode.com/users"

    with allure.step("Send GET request"):
        response = requests.get(url)

    with allure.step("Verify status code is 200"):
        assert response.status_code == 200

    with allure.step("Verify response is non-empty list"):
        data = response.json()
        assert isinstance(data, list)
        assert len(data) > 0


@allure.feature("Posts API")
@allure.title("GET /posts returns posts list")
def test_get_posts():
    url = "https://jsonplaceholder.typicode.com/posts"

    with allure.step("Send GET request"):
        response = requests.get(url)

    with allure.step("Verify response"):
        assert response.status_code == 200
        assert isinstance(response.json(), list)


@allure.feature("Todos API")
@allure.title("GET /todos returns todos list")
def test_get_todos():
    response = requests.get("https://jsonplaceholder.typicode.com/todos")

    with allure.step("Verify response"):
        assert response.status_code == 200
        assert isinstance(response.json(), list)


@allure.feature("Albums API")
@allure.title("GET /albums returns albums list")
def test_get_albums():
    response = requests.get("https://jsonplaceholder.typicode.com/albums")

    with allure.step("Verify response"):
        assert response.status_code == 200
        assert isinstance(response.json(), list)


@allure.feature("Photos API")
@allure.title("GET /photos returns photos list")
def test_get_photos():
    response = requests.get("https://jsonplaceholder.typicode.com/photos")

    with allure.step("Verify response"):
        assert response.status_code == 200
        assert isinstance(response.json(), list)


@allure.feature("Users API")
@allure.story("Get single user")
@allure.title("GET /users/1 returns user with id=1")
def test_get_user_1():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")

    with allure.step("Verify user"):
        assert response.status_code == 200
        assert response.json()["id"] == 1


@allure.feature("Posts API")
@allure.title("GET /posts/1 returns post with id=1")
def test_get_post_1():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

    with allure.step("Verify post"):
        assert response.status_code == 200
        assert response.json()["id"] == 1


@allure.feature("Todos API")
@allure.title("GET /todos/1 returns todo with id=1")
def test_get_todo_1():
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")

    with allure.step("Verify todo"):
        assert response.status_code == 200
        assert response.json()["id"] == 1


@allure.feature("Albums API")
@allure.title("GET /albums/1 returns album with id=1")
def test_get_album_1():
    response = requests.get("https://jsonplaceholder.typicode.com/albums/1")

    with allure.step("Verify album"):
        assert response.status_code == 200
        assert response.json()["id"] == 1


@allure.feature("Photos API")
@allure.title("GET /photos/1 returns photo with id=1")
def test_get_photo_1():
    response = requests.get("https://jsonplaceholder.typicode.com/photos/1")

    with allure.step("Verify photo"):
        assert response.status_code == 200
        assert response.json()["id"] == 1



