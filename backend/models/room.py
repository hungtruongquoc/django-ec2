from django.db import models

from .base_model import BaseModel
from .hotel import Hotel


class Room(BaseModel):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, default=None)
