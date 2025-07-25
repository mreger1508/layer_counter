"""
Plugin __init__.py file
Import Plugin Class from layer_counter.py
"""
from .layer_counter import LayerCounter
def classFactory(iface):
    return LayerCounter(iface)
