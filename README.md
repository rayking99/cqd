# cqd

A lightweight Python utility that provides colored visualization of object attributes, making it easier to inspect objects during development and debugging.

## Features

- Color-coded attribute display:
  - 🔵 Blue: Dunder methods
  - 🟡 Yellow: Protected attributes (starting with `_`)
  - 🟢 Green: Public attributes and methods

For example - here is a snippet of the tokenizer from huggingface.

<img src="assets/example.png" width="500" alt="example">

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

If you want to see the types, use cqd2

```python
from cqd import cqd2 as q
import math

q(math)

```

That will produce:

![alt text](assets/example2.png)

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.

## License

This project is licensed under the MIT License.
