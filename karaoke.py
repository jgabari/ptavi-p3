#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import smallsmilhandler
import json

if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()
    sHandler = smallsmilhandler.SmallSMILHandler()
    parser.setContentHandler(sHandler)
    try:
        parser.parse(open(sys.argv[1]))
    except IndexError:
        print("Usage: python3 karaoke.py file.smil")

    jsonfile = sys.argv[1].split('.')
    jsonfile = jsonfile[0] + '.json'
    with open(jsonfile, 'w') as outfile:
        json.dump(sHandler.content, outfile, indent=4)

    content = ""
    for tag in sHandler.content:
        content += tag['name'] + "\t"
        del tag['name']
        for att in tag:
            content += att + '="' + tag[att] + '"\t'
        content += '\n'
    print(content)



