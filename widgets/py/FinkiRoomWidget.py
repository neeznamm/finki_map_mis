from kivy.properties import ColorProperty
from kivymd.app import MDApp

from widgets.py.RoomWidget import RoomWidget


class FinkiRoomWidget(RoomWidget):
    """
    A room (laboratory, classroom) with a clickable label (RoomNamePill).
    On click the label will open a dialog/screen containing the
    class schedule in that room.
    """
    fill_color = ColorProperty([0.843, 0.902, 0.941, 1])

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            room_name = self.children[0].text

            app = MDApp.get_running_app()
            app.show_room_info_dialog(room_name)
        return super().on_touch_down(touch)
