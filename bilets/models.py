from django.db import models
from django.conf import settings
import uuid


class Bilets(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    invoiceId = models.UUIDField(unique=True, default=uuid.uuid4)


class Proverka(models.Model):
    invoiceId_Vvod = models.UUIDField()