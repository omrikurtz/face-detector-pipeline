from dataclasses import dataclass

"""
This is a general-purpose object, representing a Rectangle extracted from a Vision Cloud API.
This is so we have a defined model for working with the data, instead of formatting and pretty-fying it
from every endpoint we use.
"""


# TODO: Perhaps generalize this a little better? We can extract any polygon, But this fits very nicely with our model!


@dataclass
class ExtractedRect:
    vertices: list
    # Note : these aren't really tuples. These are Vertex objects from the Google SDK.
    # It is a pain in the ass to actually import Vertex for the type-hinting which dataclasses require
    # Because of how google uses dynamic imports in their SDK.
    top_left_corner: tuple
    top_right_corner: tuple
    bottom_right_corner: tuple
    bottom_left_corner: tuple
