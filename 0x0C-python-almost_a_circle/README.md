# Python - Almost a circle

Implementation of geometric rectangle and square with Python programming.

### Classes

> This project uses Object-Oriented Programming to build and connect logic.

#### Base class

The `Base` class is the fundamentatal blueprint for all object.
It provides the following attributes and methods

- `id`: A serial unique identifier for all objects created (that inherit from `Base`).
  Value may be custom instead of the automatic serial value
- `to_json_string`: A static method to get the JSON representation of a list of dictionaries.
  Each dictionary in this list is a dictionary representation of an instance that inherits from `Base`
- `from_json_string`: A static method to parse a string and get list of objects.
  Each object is an instance of a subclass of `Base`
- `create`: Given keyworded arguments, this class method creates an instance with all attributes already set.
- `load_from_file`: Class method creates a list of instances from JSON file which contains a serialized list of dictionaries.
- `save_to_file`: Class method creates a serialized list of dictionaries from list of objects and saves to a JSON file.
- `load_from_file_csv`: Class method creates a list of instances from CSV file which contains a serialized list of dictionaries.
- `save_to_file_csv`: Class method creates a serialized list of dictionaries from list of objects and saves to a CSV file.
- `draw`: Class method uses turtle to draw list of shapes (rectangles and squares) on the screen

#### Rectangle class

Inherits `Base` class

- `width`: Width attribute of rectangle object
- `height`: Height attribute of rectangle object
- `x`: X coordinate attribute of rectangle object
- `y`: Y coordinate attribute of rectangle object
- `area`: Instance method returns the area of rectangle object
- `display`: Instance method prints rectangle object to `stdout`
- `update`: Instance method updates rectangle object with `*args` and `**kwargs`
- `to_dictionary`: Instance method creates a dictionary representation of rectangle object.

#### Square class

Inherits `Rectangle` class

- `size`: Size attribute of square object. Defines both `width` and `height`
- `update`: Instance method updates square object with `*args` and `**kwargs`
- `to_dictionary`: Instance method creates a dictionary representation of square object.
