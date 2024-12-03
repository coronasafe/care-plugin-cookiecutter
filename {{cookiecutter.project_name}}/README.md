# {{cookiecutter.name}}

[![Release Status](https://img.shields.io/pypi/v/{{cookiecutter.project_name}}.svg)](https://pypi.python.org/pypi/{{cookiecutter.project_name}})
[![Build Status](https://github.com/ohcnetwork/{{cookiecutter.project_name}}/actions/workflows/build.yaml/badge.svg)](https://github.com/ohcnetwork/{{cookiecutter.project_name}}/actions/workflows/build.yaml)

{{cookiecutter.name}} is a sample plugin, a plugin boilerplate to begin developing the plugin for care.

## Local Development

To develop the plug in local environment along with care, follow the steps below:

1. Go to the care root directory and clone the plugin repository:

```bash
cd care
git clone git@github.com:ohcnetwork/{{cookiecutter.project_name}}.git
```

2. Add the plugin config in plug_config.py

```python
...

{{cookiecutter.plugin_name}}_plugin = Plug(
    name={{cookiecutter.plugin_name}}, # name of the django app in the plugin
    package_name="/app/{{cookiecutter.project_name}}", # this has to be /app/ + plugin folder name
    version="", # keep it empty for local development
    configs={}, # plugin configurations if any
)
plugs = [{{cookiecutter.plugin_name}}_plugin]

...
```

3. Tweak the code in plugs/manager.py, install the plugin in editable mode

```python
...

subprocess.check_call(
    [sys.executable, "-m", "pip", "install", "-e", *packages] # add -e flag to install in editable mode
)

...
```

4. Rebuild the docker image and run the server

```bash
make re-build
make up
```

> [!IMPORTANT]
> Do not push these changes in a PR. These changes are only for local development.

## Production Setup

To install care {{cookiecutter.plugin_name}}, you can add the plugin config in [care/plug_config.py](https://github.com/ohcnetwork/care/blob/develop/plug_config.py) as follows:

```python
...

{{cookiecutter.plugin_name}}_plug = Plug(
    name={{cookiecutter.plugin_name}},
    package_name="git+https://github.com/ohcnetwork/{{cookiecutter.project_name}}.git",
    version="@master",
    configs={},
)
plugs = [{{cookiecutter.plugin_name}}_plug]
...
```

[Extended Docs on Plug Installation](https://care-be-docs.ohc.network/pluggable-apps/configuration.html)

## Configuration

The following configurations variables are available for {{cookiecutter.name}}:

- `{{cookiecutter.plugin_name.capitalize()}}_DUMMY_ENV`: Dummy environment variable for testing

The plugin will try to find the API key from the config first and then from the environment variable.

## Cookiecutter Template Instructions

This template allows you to create a new plugin for the Care project. Below are the expected inputs:

- **`project_name`**: The full plugin name with the `care_` prefix, formatted in snake_case (e.g., `care_hello`).
- **`plugin_name`**: The plugin name only, in lowercase (e.g., `hello`).
- **`name`**: The plugin name in Title Case (e.g., `Care Hello`).
- **`description`**: A brief description of the plugin's purpose (e.g., `A Care plugin for managing user data`).
- **`version`**: The version number of the plugin in `MAJOR.MINOR.PATCH` format (e.g., `0.1.0`).

Run the template using:
```bash
cookiecutter path/to/this/template

## License

This project is licensed under the terms of the [MIT license](LICENSE).

---

This plugin was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) using the [ohcnetwork/care-plugin-cookiecutter](https://github.com/ohcnetwork/care-plugin-cookiecutter).
