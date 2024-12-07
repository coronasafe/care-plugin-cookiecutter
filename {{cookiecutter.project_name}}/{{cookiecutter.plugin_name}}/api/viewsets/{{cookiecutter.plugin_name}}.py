from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from {{cookiecutter.plugin_name}}.api.serializers.{{cookiecutter.plugin_name}} import {{cookiecutter.plugin_name.capitalize()}}Serializer
from {{cookiecutter.plugin_name}}.models.{{cookiecutter.plugin_name}} import {{cookiecutter.plugin_name.capitalize()}}


class {{cookiecutter.plugin_name.capitalize()}}Viewset(
    RetrieveModelMixin,
    ListModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    GenericViewSet
):
    queryset = {{cookiecutter.plugin_name.capitalize()}}.objects.all().order_by("-created_date")
    serializer_class = {{cookiecutter.plugin_name.capitalize()}}Serializer
    lookup_field = "external_id"
    permission_classes = [IsAuthenticated]
