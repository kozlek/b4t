from __future__ import annotations

import uuid

from django.conf import settings
from pynamodb.models import Model, MetaModel

from .attributes import UUIDAttribute


class MockQuerySet:
    __slots__ = ("model",)

    def __init__(self, model: type[BaseNoSQLModel]):
        self.model = model

    def all(self):
        return self

    def get(self, *args, pk=None, **kwargs):
        if pk is not None:
            return self.model.get(pk)
        # TODO: refine the wrapper later
        return self.model.get(*args, **kwargs)

    def count(self):
        return self.model.count()

    def __iter__(self):
        return self.model.scan()


class PatchedMetaModel(MetaModel):
    def __new__(mcs, name, bases, attrs):
        kls = super().__new__(mcs, name, bases, attrs)
        setattr(kls, "objects", MockQuerySet(model=kls))
        return kls


class BaseNoSQLModel(Model, metaclass=PatchedMetaModel):
    id = UUIDAttribute(default_for_new=uuid.uuid4, hash_key=True)

    objects: MockQuerySet

    class Meta:
        abstract = True
        host = settings.DYNAMODB_HOST
        region = settings.DYNAMODB_REGION
        read_capacity_units = 1
        write_capacity_units = 1
