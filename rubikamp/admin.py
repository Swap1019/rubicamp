from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('username','profile','first_name','last_name','is_staff','is_active')
    list_filter = (['username'])


admin.site.register(User,UserAdmin)
