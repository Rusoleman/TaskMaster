from django.contrib.auth.models import User
from django.db import models
from django.db.models import ForeignKey, SET_NULL
from cards.models import Card


class Comment(models.Model):
    message = models.TextField(null=False, blank=False)
    creation_date = models.DateTimeField()

    def __str__(self):
        return self.message  # Change the name? or add new field ?

    # ═════════ Relations ═════════
    owner = models.ForeignKey(
        User,
        null=True,
        on_delete=SET_NULL
    )
    card = models.ForeignKey(
        Card,
        null=True,
        on_delete=SET_NULL
    )




