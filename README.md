# cqd (Quick Display)

A lightweight Python utility that provides colored visualization of object attributes, making it easier to inspect objects during development and debugging.

## Features

- Color-coded attribute display:
  - 🔵 Blue: Dunder methods
  - 🟡 Yellow: Protected attributes (starting with `_`)
  - 🟢 Green: Public attributes and methods

## Installation

You can install the package using pip:

```
pip install cqd
```

## Usage

To use the `cqd` function, import it from the package:

```python
from cqd import cqd

# Example usage
cqd(your_object)
```

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.

## License

This project is licensed under the MIT License.
