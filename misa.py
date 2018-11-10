import shutil
import sys
import os

parameters = ["create", "delete", "build"]

argument = sys.argv [1]
project = sys.argv [2]
path = os.getcwd ()

projectPath = path + "/projects/" + project + "/"

newLine = "\n"
newLines = newLine * 2


def CreateMisaFiles (name):

    startComment = "//Everything Here Will Run Once"
    loopComment = "//Everything Here Will Loop"

    streamWriter = open (projectPath + name + ".ms", "w+")

    streamWriter.write ("func start ()" + newLines)
    streamWriter.write (startComment + newLines)
    streamWriter.write ("func end" + newLines)
    streamWriter.write ("func update ()" + newLines)
    streamWriter.write (loopComment + newLines)
    streamWriter.write ("func end" + newLine)

    streamWriter.close ()

    streamWriter = open (projectPath + "config.ms", "w+")

    streamWriter.write ("Misa.Name = " + "'" + name + "''" + newLine)
    streamWriter.write ("Misa.Dimensions = " + "(800, 600)" + newLine)

    streamWriter.close ()

def CreateProject (name):

    os.makedirs (path + "/projects/" + name)

    os.makedirs (projectPath + "build")
    os.makedirs (projectPath + "assets")
    os.makedirs (projectPath + "logs")

    os.makedirs (projectPath + "assets/sounds")
    os.makedirs (projectPath + "assets/sprites")

    CreateMisaFiles (name)

def DeleteProject (name):

    shutil.rmtree (path + "/projects/" + name)

    print ("Project: " + name + " Deleted")

def BuildProject (name):

    #Build Project
    hello = "hello"

if argument == parameters [0]:

    CreateProject (project)

elif argument == parameters [1]:

    DeleteProject (project)

elif argument == parameters [2]:

    BuildProject (project)
