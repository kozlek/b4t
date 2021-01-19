import pytest
from rest_framework import status

pytestmark = pytest.mark.django_db


def test_user_viewset_list(api_client, users):
    res = api_client.get("/api/v1/users/")
    assert res.status_code == status.HTTP_200_OK
    # TODO: test returned data
