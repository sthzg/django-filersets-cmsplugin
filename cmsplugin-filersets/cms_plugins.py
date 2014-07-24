# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from cmsplugin_filersets.models import DCMSFilerset


class DCMSFilersetsPlugin(CMSPluginBase):
    """
    Allow the user to select a filerset and render its contents to the
    page.
    """
    model = DCMSFilerset
    name = _('Filersets')
    render_template = "cmsplugin_filersets/filersets_gallery.html"

    def render(self, context, instance, placeholder):
        items = instance.fset.get_items_sorted()
        context['fitems'] = list()
        for item in items:
            context['fitems'].append(item.filer_file)
        return context

plugin_pool.register_plugin(DCMSFilersetsPlugin)
