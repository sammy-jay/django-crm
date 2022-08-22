from django.contrib import admin

# Register your models here.
from .models import Lead, User, Agent

admin.site.register(User)
admin.site.register(Agent)
admin.site.register(Lead)
