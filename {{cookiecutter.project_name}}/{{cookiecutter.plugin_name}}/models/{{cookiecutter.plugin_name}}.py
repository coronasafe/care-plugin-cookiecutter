from django.db import models

from care.utils.models.base import BaseModel


class {{cookiecutter.plugin_name.capitalize()}}(BaseModel):
    name = models.CharField(max_length=10)
