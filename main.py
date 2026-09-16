from datetime import datetime
from unittest import case

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window


Window.size = (300, 500)

def CheckPeriod(day):
    if day == "Friday":
        period = None
        return period
    period =
    return period

EXAMPLE_TABLE = [
    [""]
]

# dont touch this its hard coded for a reason
# array is name, start time, end time, duration
PERIOD_TIMES_MON_THURS = [
    ["Tutor Time", "8:25", "8:55", "30"],

    ["P1", "8:55", "9:50", "55"],
    ["P2", "9:50", "10:45", "55"],

    ["Break", "10:45", "11:10", "25"],

    ["P3", "11:10", "12:05", "55"],
    ["P4", "12:05", "13:00", "55"],

    ["Break", "13:00", "13:45", "45"],

    ["P3", "13:45", "14:40", "55"],
    ["P4", "14:40", "15:35", "55"],
]

class PymeTable(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)
        current_day = datetime.now().strftime("%A")
        print(current_day)

        # Title you know
        self.title = Label(text='Pyme Table', font_size=30, halign="center", valign="top")
        self.add_widget(self.title)

        self.CURRENT_PERIOD = Label(text=)

        self.grid = GridLayout(cols=1, spacing=5, padding=10)
        match current_day:
            case "Monday":
                pass
            case "Tuesday":
                pass
            case "Wednesday":
                pass
            case "Thursday":
                pass

            # this is different
            case "Friday":
                pass
        self.add_widget(self.grid)


class PymeTableApp(App):
    def build(self):
        return PymeTable()

if __name__ == "__main__":
    PymeTableApp().run()
