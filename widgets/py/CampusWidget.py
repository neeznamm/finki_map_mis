import os

from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder

Builder.load_file(os.path.join(os.path.dirname(__file__), '../kv/CampusWidget.kv'))


class CampusWidget(FloatLayout):
    """
    A direct child of MapRootWidget which shows the boundary of the
    FCSE campus. Its siblings are Labels containing names of streets
    surrounding the campus.
    """
    pass
