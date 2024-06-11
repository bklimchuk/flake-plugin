# Function dsclaration plugin for Flake8

This is a custom Flake8 plugin designed to enforce proper formatting of function definitions in Python. It ensures that function arguments are correctly aligned and formatted according to specified guidelines.

## Features

- Ensures each argument in a multi-line function definition starts on a new line.
- Ensures the closing parenthesis of the function definition aligns with the `def` keyword.
- Allows single-line function definitions for functions with zero or one argument.

## Dependencies

To install the required dependencies, run:

```sh
pip install -r requirements.txt
```

## Installation

To install the plugin, you can use `pip`:

```sh
pip install -e .
```

This command installs the plugin in editable mode, allowing you to make changes to the code and have them immediately reflected in your environment.

## Create a Wheel File

To create a `.whl` file for distribution, run the following command:

```sh
python setup.py bdist_wheel
```

This command will generate a `.whl` file in the `dist/` directory. You can use this file to install the plugin in other projects.

## Add the Plugin to Your Project

To add the plugin to your Flake8 configuration, create or update your `.flake8` file in the root of your project:

```ini
[flake8]
# Other Flake8 configurations
```

## Install the Plugin in Your Project

To install the plugin in your project using the generated `.whl` file, run:

```sh
pip install path/to/your-plugin.whl
```

Replace `path/to/your-plugin.whl` with the actual path to the generated `.whl` file.

## Testing

To run the tests for this plugin, you'll need to install the required dependencies first. You can do this by running:

```sh
pip install -r requirements.txt
```

Once the dependencies are installed, you can run the tests using `pytest`:

```sh
pytest
```

## Example

Here is an example of a properly formatted function:

```python
def properly_formatted_function(
        self,
        sdk_partner_token: str,
        user_uuid4: str = None,
        phone: str = None,
        email: str = None
):
    pass
```

And here is an example of an improperly formatted function:

```python
def improperly_formatted_function(self, sdk_partner_token: str, user_uuid4: str = None, phone: str = None, email: str = None):
    pass
```

The plugin will flag the improperly formatted function with an error message indicating that the function arguments are not properly formatted.
