# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models.pluginmodel import  CMSPlugin
from model_utils.choices import Choices
from filersets.models import Set


class DCMSFilerset(CMSPlugin):
    """
    Plugin configuration model for displaying filersets in Django CMS.
    """

    RENDER_MODES = Choices(
        ('thumbnails_with_lightbox', _('Thumbnails with colorbox')))

    render_mode = models.CharField(
        _('render mode'),
        max_length=50,
        choices=RENDER_MODES,
        blank=False,
        null=False,
        default='thumbnails_with_lightbox')

    fset = models.ForeignKey(
        Set,
        verbose_name=_('filerset'),
        help_text=_('Choose the filerset which contents you wish to be '
                    'displayed.'),
        related_name='dcmsfilerset_filerset',
        blank=False,
        null=False,
        default=None)

    def copy_relations(self, oldinstance):
        for associated_item in oldinstance.associated_item.all():
            # instance.pk = None; instance.pk.save() is the slightly odd but
            # standard Django way of copying a saved model instance
            associated_item.pk = None
            associated_item.plugin = self
            associated_item.save()

    def __unicode__(self):
        return '{} for {}'.format(self.render_mode, self.fset)