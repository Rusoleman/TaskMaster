from django.contrib.auth.models import User
from django.db import models
from lists.models import List
from members.models import Member


class Card(models.Model):
    name = models.CharField(max_length=40, default="New Card")
    description = models.CharField(max_length=255)
    creation_date = models.DateTimeField()
    limit_date = models.DateTimeField()
    position = models.IntegerField()

    def __str__(self):
        return self.name

    # ═════════ Relations ═════════
    owner = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL
    )

    list = models.ForeignKey(
        List,
        null=True,
        on_delete=models.SET_NULL
    )

    member = models.ManyToManyField(
        Member,
        related_name='cards_member'
    )