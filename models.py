#coding:utf-8

import os

from . import UPLOAD_DIR
from django.db import models
from contenttyperestrictedfilefield import ContentTypeRestrictedFileField
from django.utils.encoding import smart_unicode
from django.db.models.signals import post_save, pre_delete
from import_export import resources, fields

def path_and_rename(path):
    def wrapper(instance, filename):
        ext = filename.split('.')[-1]
        # get filename
        if instance.pk:
            filename = '{0}.{1}'.format(instance.pk, ext)
        else:
            # set filename as random string
            filename = '{0}.{1}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(path, filename)
    return wrapper

#配置描述
class ConfigInfo(models.Model):
    abbr        = models.CharField(max_length=10, primary_key=True) #缩写
    name        = models.CharField(max_length=200)   #名称
    description = models.CharField(max_length=2000, blank=True)  #描述
#     last        = models.DateTimeField(auto_now_add=True)   #配置项有增删时更新
    
    def __unicode__(self):
        return smart_unicode(self.name)    

class ConfigItemChoice(models.Model):
    name        = models.CharField(max_length=200)   #名称
    value       = models.CharField(max_length=200, blank=True)   #值
    
    def __unicode__(self):
        return smart_unicode(self.name)    
    
#配置参数描述
class ConfigItemInfo(models.Model):
    TYPE_STR = 'str'
    TYPE_SEL = 'sel'
    TYPE_FIL = 'fil'
    TYPE_CONFIG_ITEM = (
        (TYPE_STR, 'string'),
        (TYPE_SEL, 'choice'),
        (TYPE_FIL, 'file'),
    )
    
    info        = models.ForeignKey(ConfigInfo)
    
    name        = models.CharField(max_length=200)   #名称
    type        = models.CharField(max_length=3, choices=TYPE_CONFIG_ITEM, default=TYPE_STR)  #类型
    choices     = models.ManyToManyField(ConfigItemChoice, blank=True)
    empty       = models.BooleanField(default=False)  #选填
    description = models.CharField(max_length=2000, blank=True)  #描述
    group       = models.IntegerField()
    order       = models.IntegerField()
    
    def __unicode__(self):
        return smart_unicode(self.name)

#项目实例
class Project(models.Model):
    abbr        = models.CharField(max_length=10, primary_key=True) #缩写
    name        = models.CharField(max_length=200)   #名称
    description = models.CharField(max_length=2000, blank=True)  #描述
    
    def __unicode__(self):
        return smart_unicode(self.name)    
    
#项目配置实例
class Config(models.Model):
    project     = models.ForeignKey(Project)
    info        = models.ForeignKey(ConfigInfo)
    
    class Meta:
        unique_together = (("project", "info"),)
            
    def __unicode__(self):
        return smart_unicode("config:"+str(self.project)+"|"+str(self.info))    
    
#配置实例参数
class ConfigItem(models.Model):
    config      = models.ForeignKey(Config)
    item        = models.ForeignKey(ConfigItemInfo)
    value       = models.CharField(max_length=2000, blank=True)  #值
    file        = ContentTypeRestrictedFileField(max_upload_size=104857600,
                                             upload_to=path_and_rename(UPLOAD_DIR), blank=True)  #上传的文件
    last        = models.DateTimeField(auto_now=True)  #上次更新时间

    class Meta:
        unique_together = (("config", "item"),)

    def __unicode__(self):
        return smart_unicode("configitem:"+str(self.config)+"|"+str(self.item))

#导出使用
class ConfigItemExportResource(resources.ModelResource):
    ex_name = fields.Field(attribute='item__name', column_name='配置项')
    ex_value = fields.Field(attribute='value', column_name='值')
    ex_file = fields.Field(attribute='file', column_name='关联')
    ex_description = fields.Field(attribute='item__description', column_name='描述')
    
    class Meta:
        model = ConfigItem
        fields = ('ex_name', 'ex_value', 'ex_file', 'ex_description')
        export_order = ('ex_name', 'ex_value', 'ex_file', 'ex_description')
        
# @receiver(models.signals.post_save, sender=ConfigItemInfo)
# def auto_delete_file_on_delete(sender, instance, **kwargs):
#     """Deletes file from filesystem
#     when corresponding `UpFile` object is deleted.
#     """
#     if instance.file:
#         if os.path.isfile(instance.file.path):
#             os.remove(instance.file.path)
#     if instance.signed:
#         if os.path.isfile(instance.signed.path):
#             os.remove(instance.signed.path)
# #用户信息
# class User(models.Model):
#     name        = models.CharField(max_length=200)   #名称
# 
#     def __unicode__(self):
#         return self.path  
#         
# #记录信息
# class Record(models.Model):
#     user        = models.ForeignKey('User')
#     timestamp   = models.DateTimeField('upload date', auto_now_add=True)    #上传的时间
#     from_ip     = models.GenericIPAddressField(blank=True, null=True)       #上传的ip    
#     
#     def __unicode__(self):
#         return self.path  
