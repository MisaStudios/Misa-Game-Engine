import core.workflow.manager as manager
import core.scripting.parser as parser

import shutil
import sys
import os

parameters = ["create", "delete", "build"]

argument = sys.argv [1]
project = sys.argv [2]
path = os.getcwd ()

if argument == parameters [0]:

    handler.CreateProject (project)

elif argument == parameters [1]:

    handler.DeleteProject (project)

elif argument == parameters [2]:

    parser.Build (project)
