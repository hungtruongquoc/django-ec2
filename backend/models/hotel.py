from django.db import models

from .base_model import BaseModel


class Hotel(BaseModel):
    address = models.CharField(max_length=255, default=None)

    @property
    def rooms(self):
        return self.room_set.all()
