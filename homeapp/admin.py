from django.contrib import admin

from .models import *



@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created')