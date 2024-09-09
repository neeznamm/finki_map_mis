import threading

import requests
from kivy.metrics import dp
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.factory import Factory
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.menu import MDDropdownMenu
from kivy.clock import mainthread

from finki_map_mis.widgets.py.AtriumWidget import AtriumWidget
from finki_map_mis.widgets.py import FloorWidget
from finki_map_mis.widgets.py.CampusWidget import CampusWidget
from finki_map_mis.widgets.py.DiagonalLineTexturedWidget import DiagonalLineTexturedWidget
from finki_map_mis.widgets.py.FinkiRoomWidget import FinkiRoomWidget
from finki_map_mis.widgets.py.ParkWidget import ParkWidget
from finki_map_mis.widgets.py import ParkingWidget
from finki_map_mis.widgets.py.Root import Root
from finki_map_mis.widgets.py import SubduedRoomName
from finki_map_mis.widgets.py.RoomNamePill import RoomNamePill
from finki_map_mis.widgets.py.RoomWidget import RoomWidget
from finki_map_mis.widgets.py.MapRootWidget import MapRootWidget
from finki_map_mis.widgets.py.SurfaceWidget import SurfaceWidget

Window.clearcolor = (.961, .969, .973, 1)


class MapApp(MDApp):
    dialog = None

    def __init__(self, **kwargs):
        super().__init__()
        self.menu = None

    def build(self):
        Factory.register('Root', cls=Root)
        Factory.register('MapRootWidget', cls=MapRootWidget)
        Factory.register('RoomWidget', cls=RoomWidget)
        Factory.register('FinkiRoomWidget', cls=FinkiRoomWidget)
        Factory.register('DiagonalLineTexturedWidget', cls=DiagonalLineTexturedWidget)
        Factory.register('AtriumWidget', cls=AtriumWidget)
        Factory.register('ParkWidget', cls=ParkWidget)
        Factory.register('ParkingWidget', cls=ParkingWidget)
        Factory.register('RoomNamePill', cls=RoomNamePill)
        Factory.register('SubduedRoomName', cls=SubduedRoomName)
        Factory.register('CampusWidget', cls=CampusWidget)
        Factory.register('SurfaceWidget', cls=SurfaceWidget)
        Factory.register('FloorWidget', cls=FloorWidget)

        return Factory.Root()

    def open_floor_menu(self, button):
        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": f"Спрат {i}",
                "height": dp(56),
                "on_release": lambda x=i: self.change_floor_on_map(x)
            } for i in range(-1, 4)
        ]

        self.menu = MDDropdownMenu(
            caller=button,
            items=menu_items,
            width_mult=4,
        )
        self.menu.open()

    def change_floor_on_map(self, floor_number):
        self.menu.dismiss()

        map_root_widget = self.root.ids.map_root_widget

        map_root_widget.change_floor(floor_number)

        top_app_bar = self.root.ids.top_app_bar
        top_app_bar.title = f"ФИНКИ кампус (спрат {floor_number})"

    def show_room_info_dialog(self, room_name):
        threading.Thread(target=self.fetch_schedule, args=(room_name,)).start()

    def fetch_schedule(self, room_name):
        schedule_url = f"http://localhost:8081/api/schedule?roomName={room_name}"

        try:
            response = requests.get(schedule_url)
            response.raise_for_status()

            schedule_data = response.json()

            schedule_content = "\n".join([f"{course}: {time}" for course, time in schedule_data.items()])

        except requests.RequestException as e:
            schedule_content = "Грешка при барање информации за распоред"

        self.update_dialog(room_name, schedule_content)

    @mainthread
    def update_dialog(self, room_name, schedule_content):
        if not self.dialog:
            self.dialog = MDDialog(
                title=f"Распоред за {room_name}",
                type="alert",
                buttons=[
                    MDFlatButton(
                        text="CLOSE", text_color=self.theme_cls.primary_color, on_release=self.close_dialog
                    ),
                ],
            )

        self.dialog.text = schedule_content
        self.dialog.open()

    def close_dialog(self, *args):
        if self.dialog:
            self.dialog.dismiss()
            self.dialog = None


MapApp().run()
