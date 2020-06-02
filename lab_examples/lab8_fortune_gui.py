#!/usr/bin/env python3

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit
import random

class FortuneTeller(QMainWindow):
    def __init__(self):
        super(FortuneTeller, self).__init__()

        self.setWindowTitle('Fortune teller')

        # A widget to hold everything
        widget = QWidget()
        self.setCentralWidget(widget)

        # A layout - in this case, a vertical one
        layout = QVBoxLayout()
        widget.setLayout(layout)

        # Create a label (non-editable text) and add it to the vertical layout
        title_label = QLabel('All-Knowing Fortune Teller')
        layout.addWidget(title_label)

        self.name_entry = QLineEdit('Put your name in here')
        layout.addWidget(self.name_entry)
        self.name_entry.editingFinished.connect(self.update_window_title)

        # Add a button and add it to the vertical layout
        self.button = QPushButton('Give Fortune')
        layout.addWidget(self.button)
        self.button.clicked.connect(self.update_fortune)

        # Add a second label
        self.fortune_label = QLabel()
        layout.addWidget(self.fortune_label)

        self.fortunes = 0

    def update_window_title(self):
        title = "{}'s fortune".format(self.name_entry.text())
        self.setWindowTitle(title)

    def update_fortune(self):
        name = self.name_entry.text()

        if self.fortunes < 2:
            msg = 'Hello {},\nYour luck for today is: {}'.format(name, random.randint(0, 10))
            self.fortunes += 1
        else:
            msg = 'You have already received 2 fortunes today.'
        self.fortune_label.setText(msg)

if __name__ == '__main__':
    app = QApplication([])
    interface = FortuneTeller()
    interface.show()
    app.exec_()