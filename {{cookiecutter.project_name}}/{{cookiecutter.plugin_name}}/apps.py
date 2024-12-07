from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

PLUGIN_NAME = "{{cookiecutter.plugin_name}}"


class {{cookiecutter.plugin_name.capitalize()}}Config(AppConfig):
    name = PLUGIN_NAME
    verbose_name = _("{{cookiecutter.plugin_name.capitalize()}}")
