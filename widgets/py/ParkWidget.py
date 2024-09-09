from kivy.properties import ColorProperty

from finki_map_mis.widgets.py.SurfaceWidget import SurfaceWidget


class ParkWidget(SurfaceWidget):
    bg_color = ColorProperty([0.886, 0.961, 0.886, 1])
    shadow = False
