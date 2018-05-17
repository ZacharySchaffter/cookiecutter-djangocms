import logging
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from parler.admin import TranslatableAdmin
from . import models


log = logging.getLogger(__name__)


class UIAppBaseAdmin(admin.ModelAdmin):
    """
    Base Admin Class.

    This is an optional Admin base class useful for
    sharing common customizations.
    """

    pass
