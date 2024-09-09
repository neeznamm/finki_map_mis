import os

from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout

Builder.load_file(os.path.join(os.path.dirname(__file__), '../kv/Root.kv'))


class Root(FloatLayout):
    pass
