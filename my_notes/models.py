from django.contrib.auth.models import User
from django.db.models import (Model, CharField, TextField, DateTimeField)
from django.db import models

from django.conf import settings


class MyNotes(Model):
    author = models.ForeignKey(User, null=True, blank=False, on_delete=models.SET_NULL)
    title = CharField(max_length=255)
    text = TextField(blank=True)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['pk']
