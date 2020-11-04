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
        self.content = []

    def startElement(self, name, attrs):
        """
        Método que se llama cuando se abre una etiqueta
        """
        if name == 'root-layout':
            self.content.append(name)
            self.content.append({'width': attrs.get('width', ""),
                                 'height': attrs.get('height', ""),
                                 'background-color': attrs.get('background-color', "")})
        elif name == 'region':
            self.content.append(name)
            self.content.append({'id': attrs.get('id', ""),
                                 'top': attrs.get('top', ""),
                                 'bottom': attrs.get('bottom', ""),
                                 'left': attrs.get('left', ""),
                                 'right': attrs.get('right', "")})
        elif name == 'img':
            self.content.append(name)
            self.content.append({'src': attrs.get('src', ""),
                                 'region': attrs.get('region', ""),
                                 'begin': attrs.get('begin', ""),
                                 'dur': attrs.get('dur', "")})
        elif name == 'audio':
            self.content.append(name)
            self.content.append({'src': attrs.get('src', ""),
                                 'begin': attrs.get('begin', ""),
                                 'dur': attrs.get('dur', "")})
        elif name == 'textstream':
            self.content.append(name)
            self.content.append({'src': attrs.get('src', ""),
                                 'region': attrs.get('region', "")})

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
