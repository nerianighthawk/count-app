from django.db import models


class Count(models.Model):
    id: int = models.AutoField(primary_key=True)

    objects = models.Manager()
