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
        self.names = {'root-layout': ['width', 'height', 'background-color'],
                      'region': ['id', 'top', 'bottom', 'left', 'right'],
                      'img': ['src', 'region', 'begin', 'dur'],
                      'audio': ['src', 'begin', 'dur'],
                      'textstream': ['src', 'region']}

    def startElement(self, name, attrs):
        """
        Método que se llama cuando se abre una etiqueta
        """
        if name in self.names:
            self.content.append(name)
            self.content.append({})
            for attr in self.names[name]:
                self.content[-1][attr] = attrs.get(attr, "")

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
