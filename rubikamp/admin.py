from django.contrib import admin
from .models import User,UserInfo

class UserAdmin(admin.ModelAdmin):
    list_display = ('username','profile','first_name','last_name','is_staff','is_active')
    list_filter = (['username'])

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('user','website_type','user_type','extra_features','sample','color_palette','logo','text_content')
    list_filter = ('user','website_type','user_type')


admin.site.register(User,UserAdmin)
admin.site.register(UserInfo,UserInfoAdmin)
