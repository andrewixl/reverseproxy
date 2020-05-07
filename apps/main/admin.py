from django.contrib import admin
from .models import Config, Auth
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.register(Config)
admin.site.register(Auth)

class ConfigResource(resources.ModelResource):
    class Meta:
        model = Config
        exclude = ('id', 'ssl', 'sslexpire')