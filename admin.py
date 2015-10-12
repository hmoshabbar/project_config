#coding:utf-8

from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from . import models

class ConfigInfoAdmin(admin.ModelAdmin):
    pass
#     list_display = ('path', 'label')
#     list_editable = ('label',)
#     list_filter = ('user', PathFilter) 
class ConfigItemChoiceAdmin(admin.ModelAdmin):
    pass

class ConfigItemInfoResource(resources.ModelResource):
    class Meta:
        model = models.ConfigItemInfo
        
class ConfigItemInfoAdmin(ImportExportModelAdmin):
    resource_class = ConfigItemInfoResource

class ProjectAdmin(admin.ModelAdmin):
    pass

class ConfigAdmin(admin.ModelAdmin):
    pass

class ConfigItemResource(resources.ModelResource):
    class Meta:
        model = models.ConfigItem
        
class ConfigItemAdmin(ImportExportModelAdmin):
    resource_class = ConfigItemResource
 
admin.site.register(models.ConfigInfo, ConfigInfoAdmin)
admin.site.register(models.ConfigItemChoice, ConfigItemChoiceAdmin)
admin.site.register(models.ConfigItemInfo, ConfigItemInfoAdmin)
admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.Config, ConfigAdmin)
admin.site.register(models.ConfigItem, ConfigItemAdmin)

