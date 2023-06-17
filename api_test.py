import pytest
import requests

# url
api_url = "https://jsonplaceholder.typicode.com"


# тест метода GET
def test_method_get_posts():
    response = requests.get(f"{api_url}/posts")
    assert response.status_code == 200


# тест метода POST
def test_method_post_posts():
    user_id = '1'
    title = "Recently added post"
    body = "Hello World!"
    arguments = {"userId": user_id, "title": title, "body": body}
    response = requests.post(f"{api_url}/posts", arguments)
    assert response.status_code == 201
    assert response.json()["userId"] == user_id
    assert response.json()["title"] == title
    assert response.json()["body"] == body


# тест метода DELETE
def test_method_delete_posts():
    post_id = "17062023"
    response = requests.delete(f"{api_url}/posts/{post_id}")
    assert response.status_code == 200
