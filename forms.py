#coding:utf-8

from django import forms
from . import models
    
class ConfigItemForm(forms.ModelForm):
    class Meta:
        model = models.ConfigItem
#         exclude = ('pub', 'plist', 'status', 'up_date', 'from_ip')

    def __init__(self, *args, **kwargs):
        super(ConfigItemForm, self).__init__(*args, **kwargs)
        if self.instance:
            if self.instance.item.type == models.ConfigItemInfo.TYPE_SEL:
                self.fields['value'] = forms.ChoiceField(choices=[ (o.value, o.name) for o in self.instance.item.choices.all()], required=False)
#             elif self.instance.item.type == models.ConfigItemInfo.TYPE_FIL:
#                 self.fields['file'] = forms.FileField(, required=False)
            self.fields['value'].show_hidden_initial = True  #放入初始值，好方便has_changed进行判断

