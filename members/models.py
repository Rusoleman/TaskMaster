from django.db import models


class Member(models.Model):
    first_name = models.CharField(max_length=40, null=False, blank=False)
    last_name = models.CharField(max_length=40, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    password = models.CharField(max_length=40, null=False, blank=False)

    def __str__(self):
        return self.first_name

