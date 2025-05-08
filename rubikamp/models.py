# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.html import mark_safe

class User(AbstractUser):
    profile = models.ImageField(upload_to="user_profile", blank=True, null=True)
    is_ownwebsite = models.BooleanField(default=False,verbose_name='website-created')

class UserInfo(models.Model):
    user = models.ForeignKey(User,to_field='id',related_name='user',on_delete=models.CASCADE)
    website_type = models.TextField(verbose_name='type_of_the_website',blank=False,null=False)
    user_type = models.TextField(verbose_name='type_of_the_users',blank=False,null=False)
    extra_features = models.TextField(verbose_name='extra_features_needed',blank=False,null=False)
    sample = models.TextField(verbose_name='sample',blank=True,null=True)
    color_palette = models.TextField(verbose_name='color_palette',blank=True,null=True)
    logo = models.ImageField(verbose_name='website_logo',blank=True,null=True)
    text_content = models.TextField(verbose_name='text_content',blank=True,null=True)

    def logo_preview(self):
        return mark_safe(f'<img src = "{self.logo.url}" width = "120" height="120" style="border-radius: 5px"/>')
    logo_preview.short_description = 'logo'