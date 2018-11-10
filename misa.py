import shutil
import sys
import os

parameters = ["create", "delete", "build"]

argument = sys.argv [1]
project = sys.argv [2]
path = os.getcwd ()

projectPath = path + "/projects/" + project + "/"
newLine = "\n"


def CreateProject (name):

    os.makedirs (path + "/projects/" + name)

    os.makedirs (projectPath + "build")
    os.makedirs (projectPath + "assets")
    os.makedirs (projectPath + "logs")

    os.makedirs (projectPath + "assets/sounds")
    os.makedirs (projectPath + "assets/sprites")

    streamWriter = open (projectPath + name + ".ms", "w+")

    streamWriter.write ("Misa.Start()" + newLine)
    streamWriter.write ("Misa.Start()" + newLine)

    streamWriter.close ()

def DeleteProject (name):

    shutil.rmtree (path + "/projects/" + name)

    print ("Project: " + name + " Deleted")

def BuildProject (name):

    #Build Project


if argument == parameters [0]:

    CreateProject (project)

elif argument == parameters [1]:

    DeleteProject (project)

elif argument == parameters [2]:

    BuildProject (project)
