import uuid

from django.db import models
from django.db.models.options import Options
from django_extensions.db.models import TimeStampedModel


class BaseModel(TimeStampedModel):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)

    objects: models.Manager
    _meta: Options

    class Meta:
        abstract = True
