from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CoreConfig(AppConfig):
    name = 'covid_19_ph.core'
    verbose_name = _("Core")

    def ready(self):
        try:
            pass
        except ImportError:
            pass
