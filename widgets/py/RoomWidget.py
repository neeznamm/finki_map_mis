import os

from kivy.properties import ColorProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.lang import Builder

Builder.load_file(os.path.join(os.path.dirname(__file__), '../kv/RoomWidget.kv'))


class RoomWidget(AnchorLayout):
    """
    A direct child of FloorWidget (along with stairs
    and entrances symbols) which represents a room.
    May or may not contain a RoomNamePill child
    which provides interaction, depending on whether
    the room is a classroom (FinkiRoomWidget).
    """
    fill_color = ColorProperty([0.925, 0.937, 0.945, 1])
