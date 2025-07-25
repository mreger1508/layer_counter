"""
Main plugin
"""
import os

from PyQt5.QtWidgets import *
from qgis.core import *
from PyQt5.QtGui import QIcon

class LayerCounter:

    def __init__(self, iface):
        """save reference to the qgis interface"""
        self.iface = iface

    def initGui(self):
        self.toolbar = QToolBar("Layer Counter Toolbar")
        self.iface.addToolBar(self.toolbar)

        # load icon
        icon_path = os.path.join(os.path.dirname(__file__), "icon.png")
        icon = QIcon(icon_path)

        # actions to add layer counter
        self.addLayerCounterAction = QAction(icon, "Count Layers", self.iface.mainWindow())

        self.toolbar.addAction(self.addLayerCounterAction)

    def unload(self):
        self.iface.mainWindow().removeToolBar(self.toolbar)
