from kivy.graphics import Color, RoundedRectangle
from kivy.graphics.texture import Texture
from kivy.uix.widget import Widget


# noinspection PyArgumentList,PyUnusedLocal
class DiagonalLineTexturedWidget(Widget):
    """
    Decorative pattern used only in the Parking widget.
    """
    primary_color = [0, 0, 0, 255]
    secondary_color = [0, 0, 0, 255]

    def __init__(self, **kwargs):
        super(DiagonalLineTexturedWidget, self).__init__(**kwargs)

        texture = Texture.create(size=(100, 100))
        pixels = b''.join([bytes(self.primary_color) if (x/3 + y/3) % 20 < 10
                           else bytes(self.secondary_color) for y in range(100) for x in range(100)])
        texture.blit_buffer(pixels, colorfmt='rgba', bufferfmt='ubyte')

        with self.canvas:
            Color(1, 1, 1, 1)
            self.rect = RoundedRectangle(pos=self.pos, size=self.size, texture=texture)

    def on_size(self, instance, value):
        self.rect.size = value

    def on_pos(self, instance, value):
        self.rect.pos = value

    def on_fill_color(self, instance, value):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(*value)
            RoundedRectangle(pos=self.pos, size=self.size)
