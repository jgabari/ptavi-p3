#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):
    """
    Clase para manejar SMIL
    """

    def __init__(self):
        """
        Constructor. Inicializamos las variables
        """
        self.width = ""
        self.height = ""
        self.backgroundcolor = ""
        self.id = ""
        self.top = ""
        self.bottom = ""
        self.left = ""
        self.right = ""
        self.src = ""
        self.region = ""
        self.begin = ""
        self.dur = ""
        self.content = []

    def startElement(self, name, attrs):
        """
        Método que se llama cuando se abre una etiqueta
        """
        if name == 'root-layout':
            # De esta manera tomamos los valores de los atributos
            self.width = attrs.get('width', "")
            self.height = attrs.get('height', "")
            self.backgroundcolor = attrs.get('background-color', "")
        elif name == 'region':
            self.id = attrs.get('id', "")
            self.top = attrs.get('top', "")
            self.bottom = attrs.get('bottom', "")
            self.left = attrs.get('left', "")
            self.right = attrs.get('right', "")
        elif name == 'img':
            self.src = attrs.get('src', "")
            self.region = attrs.get('region', "")
            self.begin = attrs.get('begin', "")
            self.dur = attrs.get('dur', "")
        elif name == 'audio':
            self.src = attrs.get('src', "")
            self.begin = attrs.get('begin', "")
            self.dur = attrs.get('dur', "")
        elif name == 'textstream':
            self.src = attrs.get('src', "")
            self.region = attrs.get('region', "")

    def endElement(self, name):
        """
        Método que se llama al cerrar una etiqueta
        """
        if name == 'root-layout':
            # Guardar el contenido en una variable self.content
            self.content.append(name)
            self.content.append({'width': self.width, 'height': self.height, 'background-color': self.backgroundcolor})
        if name == 'region':
            self.content.append(name)
            self.content.append({'id': self.id, 'top': self.top, 'bottom': self.bottom, 'left': self.left, 'right': self.right})
        if name == 'img':
            self.content.append(name)
            self.content.append({'src': self.src, 'region': self.region, 'begin': self.begin, 'dur': self.dur})
        if name == 'audio':
            self.content.append(name)
            self.content.append({'src': self.src, 'begin': self.begin, 'dur': self.dur})
        if name == 'textstream':
            self.content.append(name)
            self.content.append({'src': self.src, 'region': self.region})

    def get_tags(self):
        """
        Método que devuelve la variable self.content
        """
        return self.content


if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()
    sHandler = SmallSMILHandler()
    parser.setContentHandler(sHandler)
    parser.parse(open('karaoke.smil'))
