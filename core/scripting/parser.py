import sys
import os

path = os.getcwd () + "/parser.py"
projects = os.path.dirname (path) + "/projects/"

parse = ""
conf = ""
tokens = []

newLine = "\n"
newLines = newLine * 2

def GetTokens (tokenFile):

    with open (tokenFile) as tokenStream:

        for token in tokenStream:

            token = token.split (" ", 1) [0]

            tokens.append (token)

def ParseConfig (name):

    conf = "import pygame" + newlines + "pygame.init ()" + newLines

    configFile = projects + name + "/config.ms"

    with open (configFile) as configStream:

        for parameter in configStream:

            if tokens [4] in parameter:

                parameter = parameter.replace (tokens [4], "").replace (tokens [7], "").replace (tokens [8], "").replace (" ". "")



def Build (name):

    GetTokens ("tokens.ms")
    ParseConfig (name)

    misaFile = projects + name + "/" + name + ".ms"

    with open (misaFile) as scriptStream:

        for line in scriptStream:

            if tokens [0] in line && tokens [1] in line:

                parse +=
