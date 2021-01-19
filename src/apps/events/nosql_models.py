from pynamodb.attributes import UnicodeAttribute, JSONAttribute

from src.utils.dynamodb.attributes import DateTimeAttribute, DjangoPrimaryKeyAttribute
from src.utils.dynamodb.nosql_models import BaseNoSQLModel


class EventModel(BaseNoSQLModel):
    event_date = DateTimeAttribute()
    appointment_id = DjangoPrimaryKeyAttribute()
    name = UnicodeAttribute()
    attributes = JSONAttribute(default={})

    class Meta(BaseNoSQLModel.Meta):
        table_name = "event"
