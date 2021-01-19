from typing import Any

from rest_framework import serializers

from .nosql_models import EventModel
from ..appointment.models import Appointment


class EventSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    event_date = serializers.DateTimeField()
    appointment_id = serializers.PrimaryKeyRelatedField(
        queryset=Appointment.objects.all()
    )
    name = serializers.CharField()
    attributes = serializers.DictField(default={})

    def create(self, validated_data: dict[str, Any]) -> EventModel:
        instance = EventModel(**validated_data)
        instance.save()
        return instance

    def update(
        self, instance: EventModel, validated_data: dict[str, Any]
    ) -> EventModel:
        update_actions = [
            getattr(instance.__class__, key).set(value)
            for key, value in validated_data.items()
        ]
        instance.update(actions=update_actions)
        return instance
