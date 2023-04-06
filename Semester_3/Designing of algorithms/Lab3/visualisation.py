from PyQt6.QtCore import *
from scrolllabel import *
import bTree1


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lab 3: B-tree")

        self.tree = bTree1.BTree(25, self)

        self.treeLabel = ScrollLabel()
        self.box = QComboBox()
        self.box.addItems(["Оберіть дію:", "Заповнити", "Вставити", "Видалити", "Знайти/Редагувати"])
        self.conButton = QPushButton("Виконати")

        self.values = QLineEdit()
        self.values.setPlaceholderText("Введіть значення")

        self.conButton.setCheckable(True)

        self.lab = QLabel()

        self.conButton.clicked.connect(self.tree.start)

        outerLayout = QHBoxLayout()
        leftLayout = QVBoxLayout()

        leftLayout.addWidget(self.box)
        leftLayout.addWidget(self.values)
        leftLayout.addWidget(self.conButton)
        leftLayout.addWidget(self.lab)

        self.setFixedSize(QSize(1000, 700))
        self.lab.setFixedSize(500, 200)
        self.treeLabel.setFixedSize(QSize(500, 700))
        outerLayout.addLayout(leftLayout)
        outerLayout.addWidget(self.treeLabel)

        container = QWidget()
        container.setLayout(outerLayout)

        self.setCentralWidget(container)
