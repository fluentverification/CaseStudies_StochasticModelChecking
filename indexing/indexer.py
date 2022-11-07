#!/usr/bin/env python3

import os

class Formats:
    PRISM = 0
    IVY = 1
    SBML = 2
    JANI = 3

o = '{'
c = '}'

def getTags(fullPath):
    return [] # TODO

def createJSONFromFolder(folder, indentationLevel = 0):
    json = "["
    tabs = "\t" * indentationLevel
    for f in os.listdir(folder):
        if os.path.isdir(folder + '/' + f) and not f.startswith('.'):
            json += f"\n{tabs}{o} \"name\":\"{f}\"\n{tabs}, \"type\":\"folder\"\n{tabs}, \"contents\":{createJSONFromFolder(folder + '/' + f, indentationLevel + 1)} {c}"
        elif os.path.isfile(folder + '/' + f):
            tags = "["
            for tag in getTags(folder + '/' + f):
                tags += f"\"tag\","
            tags = f"{tags[:len(tags) - 1]}]"
            json += f"\n{tabs}{o} \"name\":\"{f}\"\n{tabs}, \"type\":\"file\"\n{tabs}, \"tags\":{tags}{c}"
    json += "]"
    return json

if __name__=='__main__':
    print(createJSONFromFolder(os.getcwd()))

