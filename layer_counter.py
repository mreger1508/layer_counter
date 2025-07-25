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
        self.addLayerCounterAction.triggered.connect(self.count_layers)
        self.toolbar.addAction(self.addLayerCounterAction)

    def unload(self):
        self.iface.mainWindow().removeToolBar(self.toolbar)

    def count_layers(self):
        # get selected layers
        layers = self.iface.layerTreeView().selectedLayers()
        counted_selected = len(layers)

        # get all layers
        all_layers = QgsProject.instance().mapLayers().values()
        counted_all_layers = len(all_layers)

        if counted_all_layers > 1 and counted_selected > 1:
            self.iface.messageBar().pushMessage(
                'Currently selected',
                f'{counted_selected} layers of {counted_all_layers} project layers',
                Qgis.Info, 6
            )

        elif counted_all_layers == 1 and counted_selected == 1:
            self.iface.messageBar().pushMessage(
                'Currently selected',
                '1 layer of 1 project layer',
                Qgis.Info, 6
            )

        elif counted_selected == 1:
            self.iface.messageBar().pushMessage(
                'Currently selected',
                f'1 layer of {counted_all_layers} project layers',
                Qgis.Info, 6
            )

        elif counted_selected == 0:
            self.iface.messageBar().pushMessage(
                'Currently selected',
                f'0 layers selected of {counted_all_layers} project layers',
                Qgis.Info, 6
            )
