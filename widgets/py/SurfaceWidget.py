import os

from kivy.properties import ColorProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder

Builder.load_file(os.path.join(os.path.dirname(__file__), '../kv/SurfaceWidget.kv'))


class SurfaceWidget(FloatLayout):
    """
    Any "larger" area on the map: park, parking, floor of building.
    This doesn't include rooms and their labels. Also used to
    help draw non-convex buildings where it serves as a "gap".
    """
    bg_color = ColorProperty([1, 1, 1, 1])
    shadow = True
