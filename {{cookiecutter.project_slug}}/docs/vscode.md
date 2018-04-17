[Pipenv]: https://example.com "Pipenv Docs"

# VSCode

Running Django from a Docker container presents certain challenges when selecting a Python interpeter in VSCode.

This template works around this by installing the project dependencies both in the local/active Virtualenv and on the container.

## Set Workspace Python Path

__NOTE:__ First complete setup instructions in the [README.md](../README.md).

Configuring the workspace `pythonPath` is easy:

1. Press __CMD + Shift + P__ and type __"Open Workspace Settings"__
2. In the right panel add this value:

```
"python.pythonPath": "${workspaceFolder}/django/.venv"
```
