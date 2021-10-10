from django.db.models import (Model, CharField, TextField, DateTimeField, ForeignKey)
from django.db import models
#from account.forms import User
from django.conf import settings

User = settings.AUTH_USER_MODEL


class MyNotes(Model):
    author = ForeignKey(User, null=True, blank=False, on_delete=models.SET_NULL)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = CharField(max_length=255)
    text = TextField(blank=True)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['pk']


