from kivy.properties import ColorProperty

from widgets.py.DiagonalLineTexturedWidget import DiagonalLineTexturedWidget
from widgets.py.SurfaceWidget import SurfaceWidget


class ParkingWidget(SurfaceWidget, DiagonalLineTexturedWidget):
    bg_color = ColorProperty([0, 0, 0, 0])
    primary_color = [245, 245, 245, 255]
    secondary_color = [240, 240, 240, 255]
