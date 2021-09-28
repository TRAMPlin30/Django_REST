from django.db.models import (Model, CharField, TextField, DateTimeField)
from django.db import models
from account.forms import User

class MyNotes(Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = CharField(max_length=255)
    text = TextField(blank=True)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['updated']


