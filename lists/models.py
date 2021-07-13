from django.db import models
from django.db.models import SET_NULL
from boards.models import Board


class List(models.Model):
    name = models.CharField(max_length=40, default="New List")
    creation_date = models.DateTimeField()
    position = models.IntegerField()

    def __str__(self):
        return self.name

    # ═════════ Relations ═════════
    boards = models.ForeignKey(
        Board,
        null=True,
        on_delete=SET_NULL
    )
