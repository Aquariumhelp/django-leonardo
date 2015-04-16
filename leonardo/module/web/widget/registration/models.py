# -#- coding: utf-8 -#-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from leonardo.module.web.models import Widget


class RegistrationWidget(Widget):

    inline = models.BooleanField(verbose_name=_("inline"), default=False)

    class Meta:
        abstract = True
        verbose_name = _("user registration")
        verbose_name_plural = _("user registrations")