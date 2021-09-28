from django.contrib import admin
from .models import MyNotes

@admin.register(MyNotes)
class MyNotes_reg(admin.ModelAdmin):
    list_display = ['title', 'text', 'created', 'updated',]
