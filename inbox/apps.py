from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MailBoxConfig(AppConfig):
    default_auto_field = 'django.db.models.AutoField'
    name = 'inbox'
    verbose_name = _("Inbox")
