import os

from kivy.lang import Builder
from kivy.uix.scatterlayout import ScatterLayout

from finki_map_mis.widgets.py.CampusWidget import CampusWidget
from finki_map_mis.widgets.py.FloorWidget import FloorWidget

Builder.load_file(os.path.join(os.path.dirname(__file__), '../kv/MapRootWidget.kv'))


# ScatterLayout is actually Float inside Scatter,
# so first child is Float ...
# thats why self.children[0].children is iterated in methods
# and not self.children

class MapRootWidget(ScatterLayout):

    def on_kv_post(self, base_widget):
        super().on_kv_post(base_widget)
        self.set_initial_floor()

    @staticmethod
    def load_floors_kv(number):
        floors = []

        floor_instances_dir = os.path.join(os.path.dirname(__file__), f'../kv/floor_instances/{number}')

        for filename in os.listdir(floor_instances_dir):
            floors.append(Builder.load_file(f'{floor_instances_dir}/{filename}'))

        return floors

    def set_floors(self, number):
        floors_number = self.load_floors_kv(number)

        for child in self.children[0].children:
            if isinstance(child, CampusWidget):
                for floor in floors_number:
                    child.add_widget(floor)

    def set_initial_floor(self):
        self.set_floors(0)

    def change_floor(self, floor_number):
        campus_child = list(filter(lambda x: (isinstance(x, CampusWidget)), self.children[0].children))[0]

        campus_child.clear_widgets(list(filter(lambda x: (isinstance(x, FloorWidget)), campus_child.children)))

        self.set_floors(floor_number)

    def on_touch_down(self, touch):
        if touch.is_mouse_scrolling:
            if touch.button == 'scrolldown':
                self.scale = self.scale * 1.1
            elif touch.button == 'scrollup':
                self.scale = self.scale * 0.8
        else:
            super(MapRootWidget, self).on_touch_down(touch)

    pass
