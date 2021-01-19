from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from src.utils.models import BaseModel


class Appointment(BaseModel):
    name = models.CharField(_("name"), max_length=255)
    description = models.TextField(_("description"), blank=True)
    date = models.DateField(_("appointment date"))
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
