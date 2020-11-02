#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import smallsmilhandler
import json
import urllib.request


class KaraokeLocal(smallsmilhandler.SmallSMILHandler):

    def __init__(self, smilfile):
        parser = make_parser()
        sHandler = smallsmilhandler.SmallSMILHandler()
        parser.setContentHandler(sHandler)
        parser.parse(smilfile)
        self.list = sHandler.get_tags()

    def __str__(self):
        aux_list = self.list
        content_str = ""
        for tag in aux_list:
            if aux_list.index(tag) % 2 == 0:
                content_str += tag + "\t"
            else:
                for att in tag:
                    content_str += att + '="' + tag[att] + '"\t'
                content_str += '\n'
        return content_str

    def to_json(self, smilfilename, jsonfilename=""):
        if jsonfilename == "":
            jsonfilename = smilfilename.split('.')
            jsonfilename = jsonfilename[0] + '.json'
        with open(jsonfilename, 'w') as jsonfile:
            json.dump(self.list, jsonfile, indent=4)

    def do_local(self):
        for tag in self.list:
            for key in tag:
                if key == 'src':
                    if tag[key].split(':')[0] == 'http':
                        name = tag[key].split('/')[-1]
                        url = tag[key]
                        name, headers = urllib.request.urlretrieve(url, name)
                        tag[key] = name


if __name__ == "__main__":
    """
    Programa principal
    """
    try:
        smilfile = open(sys.argv[1])
    except IndexError:
        print("Usage: python3 karaoke.py file.smil")
    objeto = KaraokeLocal(smilfile)
    print(objeto)
    objeto.to_json(sys.argv[1])
    objeto.do_local()
    objeto.to_json(sys.argv[1], 'local.json')
    print(objeto)
