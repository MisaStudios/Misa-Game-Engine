import shutil
import os

current = os.getcwd () + "/manager.py"
path = os.path.dirname (current)

newLine = "\n"
newLines = newLine * 2


def CreateMisaFiles (name, projectPath):

    startComment = "//Everything Here Will Run Once"
    loopComment = "//Everything Here Will Loop"

    streamWriter = open (projectPath + name + ".misa", "w+")

    streamWriter.write ("func start ()" + newLines)
    streamWriter.write (startComment + newLines)
    streamWriter.write ("func end" + newLines)
    streamWriter.write ("func update ()" + newLines)
    streamWriter.write (loopComment + newLines)
    streamWriter.write ("func end" + newLine)

    streamWriter.close ()

    streamWriter = open (projectPath + "config.misa", "w+")

    streamWriter.write ("Misa.Name = " + "'" + name + "'" + newLine)
    streamWriter.write ("Misa.Dimensions = " + "(800, 600)" + newLine)

    streamWriter.close ()

def CreateProject (name):

    projectPath = path + "/projects/" + name + "/"

    os.makedirs (path + "/projects/" + name)

    os.makedirs (projectPath + "build")
    os.makedirs (projectPath + "assets")
    os.makedirs (projectPath + "logs")

    os.mkdir (projectPath + "assets/sounds")
    os.mkdir (projectPath + "assets/sprites")

    CreateMisaFiles (name, projectPath)

def DeleteProject (name):

    shutil.rmtree (path + "/projects/" + name)

    print ("Project: " + name + " Deleted")
