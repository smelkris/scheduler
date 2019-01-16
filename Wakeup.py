

import sys
import matplotlib.pyplot as plotlib
import matplotlib.patches as mpatches
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

from WakeupModel import *


class Wakeup(QWidget):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename
        self.model = WakeupModel(self.filename)
        self.model.get_data()
        self.tasklist = self.model.tasklist

    def process_data(self):
        total_time = 0
        task_names = []
        durations = []
        for i in range(len(self.tasklist)):
            task_names.append(f"{i+1}.{self.tasklist[i]['Task']}")
            duration = self.tasklist[i]["Duration"]
            durations.append(duration)
            total_time += duration

        # Render bar chart
        plotlib.bar(task_names, durations)
        total_time_legend = mpatches.Patch(label=f'Total Time: {total_time}')
        plotlib.legend(handles=[total_time_legend])
        plotlib.title(self.model.title)
        plotlib.show()
        sys.exit(1)


def main():
    app = QApplication(sys.argv)
    wakeup = Wakeup("Preset.json")
    wakeup.process_data()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
