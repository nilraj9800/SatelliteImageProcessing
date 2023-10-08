import sys
import os
from PySide6 import QtWidgets

from gui import MainWindow
from event_handling import Event
from chitra import Modify


if __name__ == "__main__":
    image_path = os.path.join("SatelliteImageProcessing","image", "braunchm.tif")
    mod = Modify(image_path)
    image_holder, transform = mod.open_image()
    app = QtWidgets.QApplication([])
    with open("SatelliteImageProcessing\\src\\style.qss", "r") as file:
        style_sheet = file.read()
    
    app.setStyleSheet(style_sheet)
    widget = MainWindow(image_holder, transform)
    sys.exit(app.exec())
