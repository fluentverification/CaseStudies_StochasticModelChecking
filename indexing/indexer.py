#!/usr/bin/env python3

import os

class Formats:
    PRISM = 0
    IVY = 1
    SBML = 2
    JANI = 3
    UNKNOWN = 4
    formatNames = ["Prism", "IVy", "SBML", "JANI", "Unknown"]

o = '{'
c = '}'

def getTags(fullPath):
    return [] # TODO

def getFormat(fileName):
    if fileName.endswith(".prism") or fileName.endswith(".sm"):
        return Formats.PRISM
    elif fileName.endswith(".ivy"):
        return Formats.IVY
    elif fileName.endswith(".sbml"):
        return Formats.SBML
    elif fileName.endswith(".jani"):
        return Formats.JANI
    return Formats.UNKNOWN

def createJSONFromFolder(folder, indentationLevel = 0):
    json = "["
    tabs = "\t" * indentationLevel
    tabsExtra = f"{tabs}\t"
    for f in os.listdir(folder):
        if os.path.isdir(folder + '/' + f) and not f.startswith('.'):
            json += f"\n{tabs}{o}\n{tabsExtra}\"name\":\"{f}\"\n{tabsExtra}, \"type\":\"folder\"\n{tabsExtra}, \"contents\":{createJSONFromFolder(folder + '/' + f, indentationLevel + 1)} \n{tabs}{c}"
        elif os.path.isfile(folder + '/' + f):
            tags = ""
            for tag in getTags(folder + '/' + f):
                tags += f"\"tag\","
            tags = f"[{tags[:len(tags) - 1]}]"
            fileFormatName = Formats.formatNames[getFormat(f)]
            json += f"\n{tabs}, {o}\n{tabsExtra}\"name\":\"{f}\"\n{tabsExtra}, \"type\":\"file\"\n{tabsExtra}, \"tags\":{tags}"
            json += f"\n{tabsExtra}, \"format\":\"{fileFormatName}\"\n{tabs}{c}"
    json += f"\n{tabs}]"
    return json

if __name__=='__main__':
    print(createJSONFromFolder(os.getcwd()))

