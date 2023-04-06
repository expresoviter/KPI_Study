from PyQt6.QtWidgets import *


class ScrollLabel(QScrollArea):
    def __init__(self):

        QScrollArea.__init__(self)

        self.setWidgetResizable(True)

        content = QWidget(self)
        self.setWidget(content)

        lay = QVBoxLayout(content)

        self.label = QLabel(content)
        self.label.setWordWrap(True)
        lay.addWidget(self.label)
