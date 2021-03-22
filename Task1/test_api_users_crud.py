from urllib import response
import requests
import pytest

base_url = "https://gorest.co.in"
response_get = requests.get(f"{base_url}/public-api/users/123")
response_post = requests.post(f"{base_url}/public-api/users")
response_put = requests.put(f"{base_url}/public-api/users/123")
response_patch = requests.patch(f"{base_url}/public-api/users/123")
response_delete = requests.delete(f"{base_url}/public-api/users/123")


def test_create():
    # pass
    assert response_post.status_code == 201


def test_read():
    # print(response_get.json())
    assert response_get.status_code == 200


def test_update():
    # pass
    assert response_put.status_code != 304


def test_modify():
    # pass
    assert response_patch.status_code == 304


def test_delete():
    # pass
    assert response_delete.status_code == 204

