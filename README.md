# Target and Workspace Management Script

## Overview

This Python script provides a basic framework for managing targets and workspaces. It allows users to create and manipulate targets and workspaces interactively through a command-line interface. The script features two main classes: `target` and `workspace`, and supports various commands for managing these entities.

## Classes

### `target`

The `target` class represents a network target with the following attributes:

- `ip` (str): The IP address of the target.
- `port` (int): The port number of the target.
- `scheme` (str): The URL scheme (e.g., `http`, `https`).
- `target_id` (int): An identifier for the target.
- `socket` (str): A string representation of the target's IP and port.
- `params` (dict): Parameters for the target.
- `args` (str): Arguments for the target.
- `injections` (str): Injection strings for the target.
- `username` (str): Username for authentication.
- `password` (str): Password for authentication.
- `proxy` (str): Proxy settings for the target.
- `user_agent` (str): User agent string for requests.

Methods:
- `show_target_options()`: Displays the attributes of the target.

### `workspace`

The `workspace` class represents a workspace that can contain multiple targets. It includes the following attributes:

- `name` (str): The name of the workspace.
- `workspace_id` (int): An identifier for the workspace.
- `targets` (list): A list of `target` instances associated with the workspace.

Methods:
- `workspace_help()`: Displays available commands for workspace management.
- `interact()`: Enters an interactive mode for managing targets within the workspace.

## Functions

### `main_help()`

Displays available commands for managing workspaces.

### `main()`

The main function that drives the script. It initializes the default workspace and handles user input for workspace management commands.

## Commands

### Workspace Commands

- `add <url>`: Adds a new target to the workspace. The URL can be in the format `http://<ip>:<port>` or `<ip>:<port>`.
- `set <variable> <target_id> <value>`: Sets a variable for a specific target (functionality not yet implemented).
- `edit <target_id> <params>`: Edits the parameters of a target (functionality not yet implemented).
- `show <target_id>`: Displays the details of a specific target.
- `rm <target_id>`: Removes a target from the workspace.
- `ls`: Lists all targets in the workspace.
- `help`: Displays help information for workspace commands.
- `back`: Returns to the previous menu.

### Main Commands

- `create`: Creates a new workspace.
- `set <workspace_id>`: Sets the current workspace to the specified ID.
- `rm <workspace_id>`: Removes a workspace by ID.
- `ls`: Lists all available workspaces.
- `help`: Displays help information for main commands.
- `exit`: Exits the script.

## Usage

To run the script, use the following command:

```bash
python script_name.py

