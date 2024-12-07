## Cookiecutter Template Instructions

This template allows you to create a new plugin for the Care project. Below are the expected inputs:

- **`project_name`**: The full plugin name with the `care_` prefix, formatted in snake_case (e.g., `care_hello`).
- **`plugin_name`**: The plugin name only, in lowercase (e.g., `hello`).
- **`name`**: The plugin name in Title Case (e.g., `Care Hello`).
- **`description`**: A brief description of the plugin's purpose (e.g., `A Care plugin for managing user data`).
- **`version`**: The version number of the plugin in `MAJOR.MINOR.PATCH` format (e.g., `0.1.0`).

If you don't have cookiecutter installed, run:
```bash
pip install cookiecutter
```

Run the template using:

```bash
cookiecutter gh:ohcnetwork/care-plugin-cookiecutter
```