from django.contrib import admin
from .models import Config, Auth

# Register your models here.
admin.site.register(Config)
admin.site.register(Auth)