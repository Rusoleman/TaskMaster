from django.contrib.auth.models import User
from django.db import models
from members.models import Member


class Board(models.Model):
    name = models.CharField(max_length=50, default="New Board")
    description = models.CharField(max_length=255, default="New Project")
    creation_date = models.DateTimeField()
    visibility = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    # ═════════ Relations ═════════
    favorite = models.ManyToManyField(
        User,
        related_name='boards_favorite_user'
    )
    owner = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL
    )
    members = models.ManyToManyField(
        Member,
        related_name='boards_member'
    )
