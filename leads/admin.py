from django.contrib import admin

# Register your models here.
from .models import Lead, User, Agent, UserProfile


class LeadAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'age',
                    'agent')
    fields = ['first_name', 'last_name',
              'agent', ('image', 'age'), 'description']
    list_filter = ('agent', 'updated_at')


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_active',
                    )
    list_filter = ('is_active', 'is_staff')
    fields = ['username', 'first_name', 'last_name',
              'email', 'password', ('is_active', 'is_staff')]
    #   , 'groups', 'user_permissions'


admin.site.register(User, UserAdmin)
admin.site.register(Agent)
admin.site.register(Lead, LeadAdmin)
admin.site.register(UserProfile)
