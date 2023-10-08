
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtCore import Qt
import numpy as np
from chitra import Modify
from event_handling import Event

class MainWindow(QtWidgets.QWidget):
    def __init__(self, img, transform):
        super().__init__()
        self.img = img
        self.transform = transform
        self.event_handler = Event(self.transform)
        self.setWindowTitle("ImageProcess")
        self.layout = QtWidgets.QHBoxLayout(self)
        self.menu_widget = QtWidgets.QListWidget()
        for i in range(3):
            item = QtWidgets.QListWidgetItem(f"Item {i}")
            item.setTextAlignment(Qt.AlignCenter)
            s = QtCore.QSize(20,20)
            item.setSizeHint(s)
            self.menu_widget.addItem(item)
        self.menu_widget2 = QtWidgets.QListWidget()
        image_label = self.drawItems()
        item_image = QtWidgets.QListWidgetItem(self.menu_widget2)
        image_size = QtCore.QSize(200,200)
        
        item_image.setSizeHint(image_size)
        
        self.menu_widget2.setItemWidget(item_image, image_label)
        
        self.layout.addWidget(self.menu_widget)
        self.layout.addWidget(self.menu_widget2)
        self.pressed_button()
        
        self.show()
        

    def drawItems(self):
        self.image = self.img
        height, width = self.image.shape
        bytes_per_line = width
        image_format = QtGui.QImage.Format_Grayscale8  # Change this based on your array's format

        qimage = QtGui.QImage(self.image.data, width, height, bytes_per_line, image_format)
        self.pixmap = QtGui.QPixmap.fromImage(qimage)
        self.pixmap.scaledToHeight(200, mode=Qt.SmoothTransformation)
        self.pixmap.scaledToWidth(200, mode=Qt.SmoothTransformation)
        self.label = QtWidgets.QLabel()
        self.label.setPixmap(self.pixmap)
        # self.layout.addWidget(self.label)
        self.label.mousePressEvent = self.print_coordinates
        
        return self.label
        # self.layout.addWidget(self.label)
        

    def print_coordinates(self,event):
        self.event_handler.capture_coordinate(event)

    def pressed_button(self):
        self.button = QtWidgets.QPushButton("Something")
        self.layout.addWidget(self.button)
        self.button.move(50,50)
        # self.button.clicked.connect(self.window_size)






        

        



                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          