import pytest
from rest_framework.test import APIClient

from src.apps.user.models import User


@pytest.fixture()
def api_client():
    return APIClient()


@pytest.fixture()
def users():
    return User.objects.bulk_create(
        [
            User(
                email="john.doe@bsport.io",
                first_name="John",
                last_name="Doe",
                phone="0033123456789",
            ),
            User(
                email="lea.dupont@bsport.io",
                first_name="Lea",
                last_name="Dupont",
                phone="0033123456780",
            ),
        ]
    )
