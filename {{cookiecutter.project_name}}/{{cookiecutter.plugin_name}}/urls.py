from rest_framework.routers import DefaultRouter

from {{cookiecutter.plugin_name}}.api.viewsets.{{cookiecutter.plugin_name}} import {{cookiecutter.plugin_name.capitalize()}}Viewset

router = DefaultRouter()

router.register("{{cookiecutter.plugin_name}}", {{cookiecutter.plugin_name.capitalize()}}Viewset, basename="{{cookiecutter.plugin_name}}__{{cookiecutter.plugin_name}}")

urlpatterns = router.urls
