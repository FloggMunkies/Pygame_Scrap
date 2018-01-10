import pygame as pg
import os
"""

Collection of functions and classes to ease with the use of sprites in PyGame programs.

Example:
    pass

Attributes:


TODO:
    * function to upload sprite to memory
    * function to upload multiple sprites
    * class to store basic sprite functions
    * function to handle image movement for sprites that change over time
    * Add to Github
    * Function to edit sprites (such as making background transparent or resizing)
    * Add Examples
    * Add Attributes
"""

# functions


def load_image_basic(path, color_key=None):
    """Loads a sprite in the most basic fashion with a color key included.

    Takes path to an image and loads it as an pygame image object and gets its rect dimensions.
    Uses the color key to make a certain color of the image transparent, useful for sprites but not for textures.
    Color key is optional or takes an RGB tuple, such as (255, 0, 0) for red, or -1 to grab the color in the upper-left
    pixel of the image and uses that.

    :param path: String
                    Path to image
    :param color_key: Tuple or -1, optional(None)
                    The color that's to be transparent, RGB tuple or -1 which uses the pixel in the upper-left corner
    :return: Tuple
                    Image object and image.rect()
    :raises:
    SystemExit:
                    If image fails to load

    """
    try:
        image = pg.image.load(path)
    except pg.error:
        print("Cannot load image:", path)
        raise SystemExit
    image = image.convert()
    if color_key is not None:
        if color_key is -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key, pg.locals.RLEACCEL)
    return image, image.get_rect()

# classes


class SpriteGopher:
    def __init__(self):
        # TODO implement this class
        pass
