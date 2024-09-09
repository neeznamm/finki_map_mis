# Мобилна апликација за мапа на кампусот на ФИНКИ (WIP)
## Основни функционалности
- интерактивна мапа на кампусот
- избор на спрат за кој се прикажуваат просториите
- приказ на распоред на часови за просториите на факултетот
  - комуникација со HTTP сервис

![](/screens/bigmap.png)
![](/screens/floorfunc.png)
![](/screens/schedulefunc.png)

## Развој
Потребно Python 3.11 и некој Docker runtime за сервисот за распоред
- стартување на апликацијата
  - `pip install -r requirements.txt`
  - `python3 main.py`
- стартување на сервисот за распоред
  - `docker run -p 8081:8081 -d docker.io/mladenovski/mis-dummy-schedule`

## Техничка документација
### UI
Апликацијата е изработена со [Kivy](https://kivy.org/) рамката за развој на cross-platform апликации. 
Се користи и [KivyMD](https://kivymd.readthedocs.io/en/latest/) што е библиотека со некои готови Material Design
компоненти: применета е за AppBar-от, менито за менување спратови и dialog-от што го прикажува распоредот. Останатите 
UI компоненти се custom и нивниот изглед и однесување се дефинирани во соодветните `/widgets/py/[Widget].py` фајлови. 
Каде што има потреба (пр. кога има покомплексен layout и сакаме да го опишеме декларативно), придружени им се и `/widgets/kv/[Widget].kv` фајловите.
`Root` компонентата е предок на сите widget-и:
```python
class MapApp(MDApp):
  
    def build(self):
        Factory.register('Root', cls=Root)
        Factory.register('MapRootWidget', cls=MapRootWidget)
        Factory.register('RoomWidget', cls=RoomWidget)
        ...
        Factory.register('FloorWidget', cls=FloorWidget)

        return Factory.Root()
```

### Менување спратови
Имплементирано во методите `change_floor` и `set_floors` на `MapRootWidget`:
```python
def change_floor(self, floor_number):
    campus_child = list(filter(lambda x: (isinstance(x, CampusWidget)), self.children[0].children))[0]

    campus_child.clear_widgets(list(filter(lambda x: (isinstance(x, FloorWidget)), campus_child.children)))

    self.set_floors(floor_number)

    
def set_floors(self, number):
    floors_number = self.load_floors_kv(number)

    for child in self.children[0].children:
        if isinstance(child, CampusWidget):
            for floor in floors_number:
                child.add_widget(floor)
```
На `change_floor` му се предава `floor_number` аргументот што се презема од event (`on_release`) кој се 
емитува кога корисникот ќе притисне на некоја од опциите од менито ("Спрат -1", "Спрат 0" итн.)

### Комуникација со веб сервис
Имплементирано во `show_room_info_dialog`, `fetch_schedule`,  `update_dialog` и `close_dialog` методите во `main.py`.
Во посебен thread (за да не се блокира интеракцијата) се прави HTTP барање до `/api/submissions?roomName=[име_на_просторија]`.
Потоа телото на одговорот што го содржи распоредот се парсира и се прави повик до главниот thread (`update_dialog`) да 
го рендерира dialog-от со повратните информации.\
Функцијата `show_room_info_dialog` се повикува при допир на некоја од компонентите `FinkiRoomWidget`:
```python
class FinkiRoomWidget(RoomWidget):
    ...
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            room_name = self.children[0].text

            app = MDApp.get_running_app()
            app.show_room_info_dialog(room_name)
        return super().on_touch_down(touch)

```