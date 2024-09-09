import os

from kivy.lang import Builder
from kivy.uix.label import Label

Builder.load_file(os.path.join(os.path.dirname(__file__), '../kv/SubduedRoomName.kv'))


class SubduedRoomName(Label):
    """
    An unclickable room label. Used for AtriumWidget.
    Is used on Surface subclasses too (Park and Parking).
    """
    pass
