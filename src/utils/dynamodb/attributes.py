import uuid
from datetime import datetime

from django.apps import apps
from pynamodb.attributes import UnicodeAttribute, JSONAttribute

from src.utils.models import BaseModel


class UUIDAttribute(UnicodeAttribute):
    def serialize(self, value: uuid.UUID) -> str:
        return super().serialize(value=str(value))

    def deserialize(self, value: str) -> uuid.UUID:
        return super().deserialize(value=uuid.UUID(value))


class DateTimeAttribute(UnicodeAttribute):
    def serialize(self, value: datetime) -> str:
        return super().serialize(value.isoformat())

    def deserialize(self, value: str) -> datetime:
        return super().deserialize(value=datetime.fromisoformat(value))


class DjangoPrimaryKeyAttribute(JSONAttribute):
    def serialize(self, value: BaseModel) -> str:
        return super().serialize(
            value={"model": value._meta.label, "id": str(value.id)}
        )

    def deserialize(self, value: str) -> BaseModel:
        instance_data = super().deserialize(value=value)
        model: type[BaseModel] = apps.get_model(instance_data["model"])
        return model.objects.get(id=instance_data["id"])
