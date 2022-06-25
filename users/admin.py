from django.contrib import admin
from django.contrib.auth.models import User
from .models import UserLinks, LinkDetails

# Register your models here.

admin.site.register(UserLinks)
admin.site.register(LinkDetails)
admin.site.register(User)
