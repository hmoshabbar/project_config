#coding:utf-8
from __future__ import print_function

import json

from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseNotFound
from django.forms.models import modelformset_factory, inlineformset_factory
from django.db.models import Q
from django.db import transaction
from . import forms
from . import models


def doConfigItem(request, project, config):
    the_config =  get_object_or_404(models.Config, Q(project__abbr=project) & Q(info__abbr=config))

    ConfigItemFormSet = inlineformset_factory(models.Config, models.ConfigItem, extra=0, fields=('value', 'file', ), form=forms.ConfigItemForm)
    if request.method == 'POST':
        formset = ConfigItemFormSet(request.POST, request.FILES, instance=the_config)
        if formset.is_valid():
            with transaction.atomic():
                for form in formset:
                   if form.has_changed():
                       form.save()
#             formset.save()

            result = {'success':'0'}
        else:
            result = {'err':dict(formset.errors)};
        return HttpResponse(json.dumps(result), content_type='application/json')
    else:
        #没有数据就添加数据
        query = models.ConfigItem.objects.filter(config=the_config)        
        if len(query) == 0:
            with transaction.atomic():
                for item in models.ConfigItemInfo.objects.filter(info=the_config.info).order_by('group','order'):
#                 print(str(item)+'\n')
                    it = models.ConfigItem(config=the_config, item=item)
                    it.save()

        formset = ConfigItemFormSet(instance=the_config, queryset=models.ConfigItem._default_manager.order_by('item__group', 'item__order'))
#         print(formset)
        
    return render(request, 'project_config/configitem_edit.html', {'formset': formset, 'config' : the_config})


def viewConfigItem(request, project, config):
    the_config =  get_object_or_404(models.Config, Q(project__abbr=project) & Q(info__abbr=config))
    query = models.ConfigItem.objects.filter(config=the_config).order_by('item__group', 'item__order') 
    if len(query) == 0:
        with transaction.atomic():
            for item in models.ConfigItemInfo.objects.filter(info=the_config.info).order_by('group','order'):
                it = models.ConfigItem(config=the_config, item=item)
                it.save()
    values = models.Config.objects.all().values_list('project__pk', flat=True)            
    projects = models.Project.objects.filter(pk__in=list(values))
    return render(request, 'project_config/configitem_view.html', {'query': query, 'config' : the_config, 'projects' : projects})

def exportConfigItem(request, project, config):
    the_config =  get_object_or_404(models.Config, Q(project__abbr=project) & Q(info__abbr=config))
    query = models.ConfigItem.objects.filter(config=the_config).order_by('item__group', 'item__order') 
    if len(query) == 0:
        with transaction.atomic():
            for item in models.ConfigItemInfo.objects.filter(info=the_config.info).order_by('group','order'):
#                 print(str(item)+'\n')
                it = models.ConfigItem(config=the_config, item=item)
                it.save()
    dataset = models.ConfigItemExportResource().export(query)
    response = HttpResponse(dataset.xls, content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename="%s"' % (project+'-'+config+'.xls')
    return response

def listProject(request, config):
    configinfo =  get_object_or_404(models.ConfigInfo, Q(abbr=config))
    infos = models.ConfigInfo.objects.all()
    keys=models.ConfigItemInfo.objects.filter(info=configinfo, important=True) #['项目名称', '项目经理', '服务器负责', '客户端负责']
    configs =  models.Config.objects.filter(info=config)
    query = []
    for config in configs:
        query.append((config,[models.ConfigItem.objects.get(config=config, item=key)  for key in keys]))
#     print(query)
    return render(request, 'project_config/project_view.html', {'infos' : infos, 'query': query, 'keys' : keys, 'configinfo' : configinfo, 'configs' : configs})


    
